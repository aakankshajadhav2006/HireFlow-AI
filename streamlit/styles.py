"""Presentation styles for HireFlow's public landing and authentication pages."""

import streamlit as st


def inject_marketing_styles() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

        .stApp,
        [data-testid="stAppViewContainer"],
        [data-testid="stMain"] {
            background: #2563EB !important;
            color: #111827 !important;
        }
        .block-container {
            box-sizing: border-box;
            max-width: 1420px;
            flex-shrink: 0;
            min-height: calc(100vh - 64px);
            margin: 32px auto;
            padding: 1rem clamp(1.25rem, 4vw, 3.75rem) 3rem;
            border-radius: 12px;
            background: #EFF6FF;
        }
        .stApp, .stApp button, .stApp input {
            font-family: 'Inter', sans-serif;
        }
        h1, h2, h3, .hf-brand {
            font-family: 'Inter', sans-serif !important;
            color: #111827 !important;
        }
        .stButton > button, .stFormSubmitButton > button {
            min-height: 2.75rem;
            padding: .6rem 1.2rem !important;
            border: 1px solid transparent !important;
            border-radius: 999px !important;
            font-weight: 600 !important;
            box-shadow: none !important;
            transition: background-color .18s ease, color .18s ease, border-color .18s ease;
        }
        .stButton > button[kind="primary"],
        .stFormSubmitButton > button[kind="primary"] {
            background: #2563EB !important;
            color: #fff !important;
        }
        .stButton > button[kind="primary"]:hover,
        .stFormSubmitButton > button[kind="primary"]:hover {
            background: #1D4ED8 !important;
            color: #fff !important;
        }
        .stButton > button[kind="secondary"] {
            border-color: #D8E3F0 !important;
            background: #fff !important;
            color: #334155 !important;
        }
        .stButton > button[kind="secondary"] * {
            color: #334155 !important;
        }
        .stButton > button[kind="secondary"]:hover {
            border-color: #93B4EE !important;
            background: #F8FAFC !important;
            color: #1D4ED8 !important;
        }
        .stButton > button[kind="secondary"]:hover * {
            color: #1D4ED8 !important;
        }
        .hf-brand {
            display: flex;
            align-items: center;
            color: #111827 !important;
            font-size: 1.08rem;
            font-weight: 750;
            letter-spacing: -.04em;
            white-space: nowrap;
        }
        .hf-brand-mark {
            display: inline-grid;
            width: 32px;
            height: 32px;
            margin-right: .55rem;
            place-items: center;
            border-radius: 8px;
            background: #2563EB;
            color: #fff;
            font-size: .92rem;
            font-weight: 700;
        }
        .hf-gradient-text {
            margin-left: .22rem;
            color: #2563EB !important;
        }
        .hf-nav {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: clamp(1rem, 2.5vw, 2.25rem);
            white-space: nowrap;
            font-size: .87rem;
        }
        .hf-nav a {
            color: #475569 !important;
            text-decoration: none;
            transition: color .18s ease;
        }
        .hf-nav a:hover {
            color: #2563EB !important;
        }
        .hf-hero {
            padding: 2.35rem 1rem 1.35rem;
            text-align: center;
        }
        .hf-eyebrow {
            display: inline-block;
            padding: .42rem .85rem;
            border: 1px solid #D7E5FB;
            border-radius: 999px;
            background: #F8FBFF;
            color: #2563EB !important;
            font-size: .75rem;
            font-weight: 600;
        }
        .hf-hero h1 {
            margin: 1rem 0 .85rem;
            color: #111827 !important;
            font-size: clamp(2.5rem, 5vw, 4.25rem);
            font-weight: 800 !important;
            letter-spacing: -.065em;
            line-height: 1.08;
        }
        .hf-hero h1 span {
            color: #111827 !important;
        }
        .hf-hero h1 strong {
            color: #2563EB !important;
            font-weight: 800;
        }
        .hf-copy {
            max-width: 680px;
            margin: 0 auto;
            color: #64748B !important;
            font-size: .99rem;
            line-height: 1.7;
        }
        .hf-explore-button {
            display: flex;
            min-height: 2.75rem;
            align-items: center;
            justify-content: center;
            margin-top: .15rem;
            padding: .6rem 1.2rem;
            border: 1px solid #D8E3F0;
            border-radius: 999px;
            background: #fff;
            color: #1F2937 !important;
            font-size: .9rem;
            font-weight: 600;
            text-decoration: none !important;
            transition: background-color .18s ease, border-color .18s ease;
        }
        .hf-explore-button:hover {
            border-color: #93B4EE;
            background: #F8FAFC;
        }
        .hf-solutions {
            padding: .15rem 0 .65rem;
        }
        .hf-solutions h2 {
            margin: 0 0 .85rem;
            color: #111827 !important;
            font-size: clamp(1.75rem, 2.6vw, 2.35rem);
            font-weight: 750 !important;
            letter-spacing: -.05em;
            line-height: 1.18;
        }
        .hf-solutions .hf-lead {
            margin: 0 0 .65rem;
            color: #334155 !important;
            font-size: 1rem;
            font-weight: 600;
            line-height: 1.55;
        }
        .hf-solutions .hf-description {
            margin: 0 0 1.2rem;
            color: #64748B !important;
            font-size: .91rem;
            line-height: 1.7;
        }
        .hf-audience-label {
            margin-bottom: .45rem;
            color: #64748B;
            font-size: .76rem;
            font-weight: 600;
        }
        [data-testid="stImage"] img {
            width: 100%;
            aspect-ratio: 1.48;
            border-radius: 16px;
            object-fit: cover;
        }
        .hf-auth-wrap {
            max-width: 490px;
            margin: 3rem auto 1.25rem;
        }
        .hf-auth-heading {
            margin-bottom: 1.3rem;
            text-align: center;
        }
        .hf-auth-heading h1 {
            margin: .6rem 0;
            color: #111827 !important;
            font-size: 2rem;
            letter-spacing: -.05em;
        }
        .hf-auth-heading p {
            color: #64748B !important;
        }
        .hf-section-kicker {
            color: #2563EB !important;
            font-size: .75rem;
            font-weight: 650;
        }
        [data-testid="stForm"] {
            padding: 1.35rem;
            border: 1px solid #DCE7F5;
            border-radius: 16px;
            background: #fff;
            box-shadow: none;
        }
        [data-testid="stTextInput"] input {
            border-radius: 9px;
        }
        html {
            scroll-behavior: smooth;
            scroll-padding-top: 1rem;
        }
        @media (max-width: 850px) {
            .block-container {
                margin: 20px auto;
                padding: 1rem 1.5rem 2.5rem;
            }
            .hf-nav {
                gap: 1rem;
            }
            div[data-testid="stHorizontalBlock"]:has(.hf-solutions) {
                flex-direction: column;
            }
        }
        @media (max-width: 560px) {
            .block-container {
                min-height: calc(100vh - 24px);
                margin: 12px;
                padding: .85rem 1rem 2rem;
            }
            .hf-nav {
                flex-wrap: wrap;
                white-space: normal;
                font-size: .8rem;
            }
            .hf-hero {
                padding: 2rem .15rem 1rem;
            }
            .hf-hero h1 {
                font-size: clamp(2.1rem, 9vw, 3rem);
            }
            .hf-solutions h2 {
                font-size: 1.75rem;
            }
            [data-testid="stImage"] img {
                aspect-ratio: 1.25;
            }
        }
        @media (prefers-reduced-motion: reduce) {
            *, *::before, *::after {
                scroll-behavior: auto !important;
                transition-duration: .01ms !important;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
