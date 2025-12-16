import os
import streamlit as st

def load_env():
    if hasattr(st, "secrets"):
        os.environ["GROQ_API_KEY"] = st.secrets.get("GROQ_API_KEY", "")
        os.environ["SERPER_API_KEY"] = st.secrets.get("SERPER_API_KEY", "")
        os.environ["VIDEO_API_KEY"] = st.secrets.get("VIDEO_API_KEY", "")

