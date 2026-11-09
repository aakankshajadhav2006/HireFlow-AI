"""Local SQLite account storage and password verification for HireFlow."""

import hashlib
import hmac
import re
import secrets
import sqlite3
from contextlib import closing
from pathlib import Path

DATABASE_PATH = Path(__file__).resolve().parent.parent / "data" / "hireflow_users.sqlite3"
PBKDF2_ITERATIONS = 600_000
PASSWORD_MIN_LENGTH = 8
PASSWORD_MAX_LENGTH = 1024
_EMAIL_PATTERN = re.compile(r"^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$", re.IGNORECASE)


class AuthStorageError(RuntimeError):
    """Raised when account storage cannot be accessed."""


def normalize_email(email: str) -> str:
    return email.strip().lower()


def _validate_account(full_name: str, email: str, password: str) -> str | None:
    if not full_name.strip():
        return "Please enter your full name."
    if len(full_name.strip()) > 100:
        return "Full name must be 100 characters or fewer."
    normalized_email = normalize_email(email)
    if len(normalized_email) > 254 or not _EMAIL_PATTERN.fullmatch(normalized_email):
        return "Please enter a valid email address."
    if len(password) < PASSWORD_MIN_LENGTH:
        return f"Password must be at least {PASSWORD_MIN_LENGTH} characters long."
    if len(password) > PASSWORD_MAX_LENGTH:
        return "Password must be 1024 characters or fewer."
    return None


def _connect() -> sqlite3.Connection:
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DATABASE_PATH, timeout=10)
    connection.row_factory = sqlite3.Row
    return connection


def _initialize_database() -> None:
    try:
        with closing(_connect()) as connection:
            with connection:
                connection.execute(
                    """
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        full_name TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE COLLATE NOCASE,
                        password_hash TEXT NOT NULL,
                        password_salt TEXT NOT NULL,
                        password_iterations INTEGER NOT NULL,
                        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                    )
                    """
                )
    except (OSError, sqlite3.Error) as exc:
        raise AuthStorageError("Account storage is unavailable.") from exc


def _password_digest(password: str, salt: bytes, iterations: int = PBKDF2_ITERATIONS) -> bytes:
    return hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations)


def create_account(full_name: str, email: str, password: str) -> str | None:
    """Create an account; return a validation/duplicate message, or None on success."""
    error = _validate_account(full_name, email, password)
    if error:
        return error

    _initialize_database()
    salt = secrets.token_bytes(16)
    digest = _password_digest(password, salt)
    try:
        with closing(_connect()) as connection:
            with connection:
                connection.execute(
                    """
                    INSERT INTO users
                        (full_name, email, password_hash, password_salt, password_iterations)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        full_name.strip(),
                        normalize_email(email),
                        digest.hex(),
                        salt.hex(),
                        PBKDF2_ITERATIONS,
                    ),
                )
    except sqlite3.IntegrityError:
        return "An account with this email already exists. Please log in instead."
    except (OSError, sqlite3.Error) as exc:
        raise AuthStorageError("Account storage is unavailable.") from exc
    return None


def verify_credentials(email: str, password: str) -> dict[str, str] | None:
    """Return public user details for valid credentials, otherwise None."""
    if len(password) > PASSWORD_MAX_LENGTH:
        return None
    _initialize_database()
    try:
        with closing(_connect()) as connection:
            with connection:
                user = connection.execute(
                    """
                    SELECT full_name, email, password_hash, password_salt, password_iterations
                    FROM users
                    WHERE email = ?
                    """,
                    (normalize_email(email),),
                ).fetchone()
    except (OSError, sqlite3.Error) as exc:
        raise AuthStorageError("Account storage is unavailable.") from exc

    if user is None:
        _password_digest(password, b"\x00" * 16)
        return None

    salt = bytes.fromhex(user["password_salt"])
    expected = bytes.fromhex(user["password_hash"])
    actual = _password_digest(password, salt, user["password_iterations"])
    if not hmac.compare_digest(actual, expected):
        return None

    return {"full_name": user["full_name"], "email": user["email"]}
