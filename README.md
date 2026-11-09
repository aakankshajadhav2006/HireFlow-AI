# HireFlow AI — Intelligent Candidate Search & Evaluation

HireFlow AI is an AI-powered recruitment platform designed to help recruiters discover and evaluate candidates against job requirements. It combines document processing, semantic vector search, and AI-assisted evaluation to go beyond traditional keyword-based matching.

The project includes a public-facing landing page, user authentication, and a Streamlit recruitment dashboard.

---

## 🚀 Features

### 🌐 Public Homepage
- Professional public landing page for HireFlow AI.
- Blue-framed layout with a centered hero section.
- Responsive two-column content section.
- Navigation with Login, Sign Up, and product exploration options.
- Locally bundled workplace photograph.

### 🔐 User Authentication
- User registration and login using SQLite.
- Passwords stored using PBKDF2 hashing.
- Session-based authentication using Streamlit session state.
- Logout functionality.
- Protected access to the recruitment dashboard.

### 📄 Resume Processing
- Upload PDF resumes.
- Extract resume text using PDF processing.
- Parse candidate information using AI-powered processing.
- Extract skills, experience, education, and other relevant information.

### 🔎 Intelligent Candidate Search
- Semantic search using Pinecone vector database.
- Hybrid search combining semantic retrieval and keyword-based matching.
- Candidate filtering and re-ranking.
- Search candidates based on job descriptions and required skills.

### 🤖 AI-Powered Candidate Evaluation
- AI-assisted candidate evaluation.
- Candidate strengths and skill gaps.
- Job-description-based candidate assessment.
- Evaluation summaries and insights.

### 📊 Recruitment Dashboard
- Streamlit-based recruiter interface.
- Resume upload and processing.
- Candidate search and evaluation.
- Organized application workflow.

---

## 🏗️ Project Architecture

```text
HireFlow/
│
├── core/
│   ├── ingestion.py
│   ├── parsing.py
│   ├── indexing.py
│   ├── retrieval.py
│   ├── filters.py
│   ├── evaluation.py
│   └── re_ranker.py
│
├── data/
│   ├── resumes/
│   ├── jds/
│   └── hireflow_users.sqlite3
│
├── docs/
├── prompts/
│
├── streamlit/
│   ├── app.py
│   ├── home.py
│   ├── auth.py
│   └── styles.py
│
├── utils/
│   ├── config.py
│   ├── schemas.py
│   ├── embeddings.py
│   └── utils.py
│
├── assets/
│   └── hiring-team.jpg
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

*Note: This is the documented logical structure. Adjust file locations if they differ in your actual repository.*

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend development |
| Streamlit | Web interface |
| SQLite | User authentication database |
| LangChain | Document processing and LLM orchestration |
| Google Gemini | AI-powered parsing and evaluation |
| Pinecone | Vector database |
| Pydantic | Data validation |
| PyPDF | PDF text extraction |
| Git & GitHub | Version control |

---

## ⚙️ How HireFlow Works

1. **Document Ingestion:** Resume PDFs and job descriptions are loaded.
2. **Text Extraction:** Text is extracted from uploaded documents.
3. **AI Parsing:** Gemini and LangChain components process documents and extract structured information.
4. **Embedding Generation:** Document content is converted into vector embeddings.
5. **Vector Indexing:** Embeddings are stored in Pinecone.
6. **Candidate Retrieval:** Relevant candidates are retrieved based on job requirements.
7. **Filtering & Re-ranking:** Candidates are filtered and ranked using the available search components.
8. **AI Evaluation:** Candidate profiles are evaluated against job descriptions.
9. **Results:** Recruiters review candidate matches, strengths, gaps, and evaluation insights.

---

## 🔐 Authentication System

HireFlow AI includes a user authentication system built using Python, Streamlit, and SQLite.

### Authentication Components

| Component | Responsibility |
|---|---|
| `home.py` | Public landing page |
| `auth.py` | Login and registration logic |
| SQLite | Stores user account information |
| `app.py` | Controls dashboard access |

### Login Workflow

1. User opens the HireFlow homepage.
2. User selects Login.
3. Login form collects email and password.
4. `auth.py` processes the authentication request.
5. Submitted credentials are checked against the SQLite database.
6. On successful authentication, the user session is established.
7. The user can access the recruitment dashboard.
8. Invalid credentials display an error message.

### Registration Workflow

1. User selects Sign Up.
2. Registration form collects account details.
3. Authentication module processes registration.
4. Account information is saved in SQLite.
5. User can log in using registered credentials.

### Security and Session Management

- Passwords are stored using PBKDF2 hashing.
- Authentication uses Streamlit session state.
- Login sessions are limited to the current browser session.
- Persistent remember-me authentication is not enabled.
- Logging out returns the user to the public homepage.

---

## 📋 Prerequisites

Before running the project, install:

- Python
- Git
- Google Gemini API key
- Pinecone account and API key

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the Project Directory

```powershell
cd hireflow-main
```

### 3. Create a Virtual Environment

```powershell
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```powershell
pip install -r requirements.txt
```

---

## 🔑 Environment Configuration

Create a `.env` file in the project root directory.

Add your API credentials and configuration:

```env
# Google Gemini API
GOOGLE_API_KEY=your_google_api_key_here

# Pinecone API
PINECONE_API_KEY=your_pinecone_api_key_here

# Pinecone Configuration
PINECONE_INDEX_NAME=hireflow
PINECONE_DIMENSION=3072
PINECONE_METRIC=cosine

# LLM Configuration
LLM_MODEL=your_configured_gemini_model

# Processing
MAX_TEXT_LENGTH=4000

# Logging
LOG_LEVEL=INFO
```

**Important:**
- Replace placeholders with your actual credentials locally.
- Never upload your `.env` file to GitHub.
- Check `utils/config.py` for the exact configuration variables and values required by your version.
- Ensure the Pinecone index dimension matches the configured embedding model.

---

## ▶️ Running the Application

Run the following commands from the project root directory.

### Windows PowerShell

**Step 1: Navigate to the project**

```powershell
cd C:\path\to\hireflow-main
```

**Step 2: Activate the virtual environment**

```powershell
.\venv\Scripts\Activate.ps1
```

**Step 3: Start the Streamlit application**

```powershell
python -m streamlit run streamlit/app.py
```

**Step 4: Open in your browser**

```text
http://localhost:8501
```

### Stop the Application

Press `Ctrl + C` in the terminal.

---

## 💻 Using HireFlow AI

1. Open the HireFlow public homepage.
2. Register a new account or log in.
3. Access the recruitment dashboard.
4. Upload candidate resumes in PDF format.
5. Enter the job title and job description.
6. Search for relevant candidates.
7. Review candidate information and matching results.
8. Explore AI-generated candidate evaluation insights.

---

## 🔧 Configuration

Application configuration is managed through `utils/config.py` and environment variables.

Important configuration areas:

- Pinecone index name and embedding dimension.
- Gemini language model selection.
- Text processing limits.
- Logging configuration.
- API credentials.

---

## 🔒 Security Notes

- Never commit `.env` files or API keys.
- Never upload your virtual environment.
- Do not commit private resumes or personal candidate information.
- Exclude local SQLite databases from public version control.
- Store deployment credentials using your hosting platform's secrets management.
- Rotate API keys immediately if they are accidentally exposed.

### Suggested `.gitignore`

```gitignore
# Environment variables
.env
.env.*
!.env.example

# Virtual environments
venv/
.venv/

# Python cache
__pycache__/
*.py[cod]

# Local databases
*.sqlite
*.sqlite3
*.db

# Private candidate documents
data/resumes/*
data/jds/*

# Logs
*.log

# Editor settings
.vscode/
.idea/
```

Review the ignore rules before committing. Only include sample documents that you have permission to publish.

---

## 🧪 Testing

Check Python syntax:

```powershell
python -m py_compile streamlit/app.py
```

Run additional tests if available:

```powershell
python test_system.py
```

---

## 🚧 Current Development Status

### Implemented Components

- LangChain-based document processing.
- Resume and job-description parsing.
- Pinecone vector indexing.
- Semantic candidate retrieval.
- Candidate filtering and re-ranking components.
- AI-assisted candidate evaluation.
- Streamlit recruitment dashboard.
- Public landing page.
- Responsive homepage styling.
- SQLite-based user authentication.
- Login, registration, and logout flow.
- Session-based dashboard access.
- Deferred recruitment backend initialization.

### Future Improvements

- Cloud deployment.
- Persistent cloud database for user accounts.
- Improved candidate matching and ranking accuracy.
- Enhanced error handling and testing.
- Improved candidate management features.
- Production-ready security and data storage.

---

## 👩‍💻 Author

**Aakanksha Jadhav**

B.Tech Computer Science and Engineering — 2027

GitHub: [aakankshajadhav2006](https://github.com/aakankshajadhav2006)

---

**HireFlow AI — Intelligent Candidate Search & Evaluation**

*Helping recruiters discover relevant talent through intelligent search and AI-assisted evaluation.*