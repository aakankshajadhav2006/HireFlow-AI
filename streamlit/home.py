"""Public landing and authentication page layouts."""

from pathlib import Path

import streamlit as st

from styles import inject_marketing_styles

WORKPLACE_IMAGE = Path(__file__).resolve().parent / "assets" / "hiring-team.jpg"


def _go(route: str) -> None:
    st.session_state["route"] = route
    st.rerun()


def _brand() -> None:
    st.markdown(
        '<div class="hf-brand"><span class="hf-brand-mark">H</span>HireFlow <span class="hf-gradient-text">AI</span></div>',
        unsafe_allow_html=True,
    )


def render_landing_page() -> None:
    inject_marketing_styles()
    st.markdown('<div id="top"></div>', unsafe_allow_html=True)
    nav_brand, nav_links, nav_login, nav_start = st.columns(
        [1.25, 2.6, 0.8, 1.2], vertical_alignment="center"
    )
    with nav_brand:
        _brand()
    with nav_links:
        st.markdown(
            '<nav class="hf-nav" aria-label="Main navigation">'
            '<a href="#platform">Platform</a><a href="#solutions">Solutions</a>'
            '<a href="#pricing">Pricing</a></nav>',
            unsafe_allow_html=True,
        )
    with nav_login:
        if st.button("Log in", key="home_login", type="secondary", use_container_width=True):
            _go("login")
    with nav_start:
        if st.button("Start Hiring", key="home_signup", type="primary", use_container_width=True):
            _go("signup")

    st.markdown(
        """
        <section class="hf-hero" id="platform" aria-labelledby="hero-title">
          <div class="hf-eyebrow">Smart Recruitment Platform</div>
          <h1 id="hero-title"><span>Hire Talent Faster</span> <strong>Without</strong><br>
            <strong>Agencies</strong></h1>
          <p class="hf-copy">Connect with talented professionals, streamline hiring, and build your team faster with an intelligent recruitment platform.</p>
        </section>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div id="pricing"></div>', unsafe_allow_html=True)
    action_left, action_start, action_explore, action_right = st.columns(
        [1, 1.35, 1.55, 1], gap="small"
    )
    with action_start:
        if st.button("Start Hiring", key="hero_signup", type="primary", use_container_width=True):
            _go("signup")
    with action_explore:
        st.markdown(
            '<a class="hf-explore-button" href="#solutions">Explore Platform</a>',
            unsafe_allow_html=True,
        )

    text_column, image_column = st.columns(
        [0.92, 1.08], gap="large", vertical_alignment="center"
    )
    with text_column:
        st.markdown(
            """
            <section class="hf-solutions" id="solutions" aria-labelledby="solutions-title">
              <h2 id="solutions-title">A Smarter Way to Find Talent</h2>
              <p class="hf-lead">Traditional hiring is slow, expensive, and inefficient.</p>
              <p class="hf-description">HireFlow helps recruiters identify relevant candidates through intelligent resume parsing, hybrid search, and AI-assisted candidate evaluation.</p>
              <div class="hf-audience-label">Built for</div>
            </section>
            """,
            unsafe_allow_html=True,
        )
        category_columns = st.columns(3, gap="small")
        selected_audience = st.session_state.setdefault("landing_audience", "Companies")
        for column, audience in zip(category_columns, ("Companies", "Recruiters", "Talent")):
            with column:
                if st.button(
                    audience,
                    key=f"audience_{audience.lower()}",
                    type="primary" if selected_audience == audience else "secondary",
                    use_container_width=True,
                ):
                    st.session_state["landing_audience"] = audience
                    st.rerun()

    with image_column:
        if not WORKPLACE_IMAGE.is_file():
            st.error(f"Required landing-page image is missing: {WORKPLACE_IMAGE}")
        else:
            st.image(str(WORKPLACE_IMAGE), use_container_width=True)


def render_login_page() -> tuple[str, str] | None:
    inject_marketing_styles()
    form_generation = st.session_state.get("_auth_form_generation", 0)
    st.markdown('<div class="hf-auth-wrap"><div class="hf-auth-heading"><div class="hf-section-kicker">Welcome back</div><h1>Log in to HireFlow</h1><p>Continue to your candidate workspace.</p></div></div>', unsafe_allow_html=True)
    notice = st.session_state.pop("auth_notice", None)
    if notice:
        st.success(notice)
    error = st.session_state.pop("auth_error", None)
    if error:
        st.error(error)
    left, center, right = st.columns([1, 1.35, 1])
    with center:
        with st.form("login_form", clear_on_submit=True):
            email = st.text_input("Email address", key=f"login_email_{form_generation}", autocomplete="email")
            password = st.text_input(
                "Password",
                type="password",
                key=f"login_password_{form_generation}",
                autocomplete="current-password",
            )
            submitted = st.form_submit_button("Log in", type="primary", use_container_width=True)
        if st.button("Create an account", key="login_to_signup", use_container_width=True):
            _go("signup")
        if st.button("← Back to home", key="login_to_home"):
            _go("home")
    if submitted:
        return email, password
    return None


def render_signup_page() -> tuple[str, str, str, str] | None:
    inject_marketing_styles()
    form_generation = st.session_state.get("_auth_form_generation", 0)
    st.markdown('<div class="hf-auth-wrap"><div class="hf-auth-heading"><div class="hf-section-kicker">Get started</div><h1>Create your account</h1><p>Set up your HireFlow workspace in a few moments.</p></div></div>', unsafe_allow_html=True)
    error = st.session_state.pop("auth_error", None)
    if error:
        st.error(error)
    left, center, right = st.columns([1, 1.35, 1])
    with center:
        with st.form("signup_form", clear_on_submit=True):
            full_name = st.text_input("Full name", key=f"signup_name_{form_generation}", autocomplete="name")
            email = st.text_input("Email address", key=f"signup_email_{form_generation}", autocomplete="email")
            password = st.text_input("Password", type="password", key=f"signup_password_{form_generation}", autocomplete="new-password")
            confirmation = st.text_input("Confirm password", type="password", key=f"signup_confirmation_{form_generation}", autocomplete="new-password")
            submitted = st.form_submit_button("Create account", type="primary", use_container_width=True)
        if st.button("Already have an account? Log in", key="signup_to_login", use_container_width=True):
            _go("login")
        if st.button("← Back to home", key="signup_to_home"):
            _go("home")
    if submitted:
        return full_name, email, password, confirmation
    return None
