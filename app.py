import streamlit as st
from helper import load_env
load_env()

from crew.crew_runner import run_content_crew
from utils.pdf_generator import generate_pdf

st.set_page_config(page_title="AI Professional Content Creator", layout="wide")

st.title("🤖 AI Professional Content Creator")
st.caption("Multi-Agent CrewAI powered content engine")

# ---------- Inputs ----------
topic = st.text_input("Enter topic or website URL", placeholder="Cybersecurity in India")
language = st.selectbox("Select language", ["English"])

if "crew_result" not in st.session_state:
    st.session_state.crew_result = None

# ---------- Generate ----------
if st.button("🚀 Generate Professional Content"):
    with st.spinner("CrewAI agents are working..."):
        st.session_state.crew_result = run_content_crew(topic)

# ---------- Display ----------
if st.session_state.crew_result:
    result = st.session_state.crew_result

    st.markdown("## 📝 Professional Blog Article")
    st.markdown(result.article)

    st.markdown("---")
    st.markdown("## 📣 Social Media Posts")

    for post in result.social_media_posts:
        st.subheader(post.platform)
        st.write(post.content)

    # ---------- PDF ----------
    pdf_bytes = generate_pdf(
        content={
            "Blog": result.article,
            **{p.platform: p.content for p in result.social_media_posts},
        },
        language=language,
    )

    st.download_button(
        label="📥 Download Professional PDF",
        data=pdf_bytes,
        file_name="AI_Professional_Content.pdf",
        mime="application/pdf",
    )
