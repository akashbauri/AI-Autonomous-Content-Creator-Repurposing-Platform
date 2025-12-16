import streamlit as st
from crewai import Crew
from utils.pdf_generator import generate_pdf
from utils.web_scraper import extract_website_content
from utils.video_generator import generate_ai_video
from main_crew import run_crew

st.set_page_config(
    page_title="AI Content Creator",
    page_icon="🤖",
    layout="wide"
)

st.sidebar.markdown("""
### 🤖 AI Content Creator  
**Developed by Akash Bauri**  
AI Engineer | LLM Automation
""")

st.title("AI Autonomous Content Creator 🚀")

input_type = st.radio(
    "Choose input type:",
    ["Topic", "Website URL"]
)

user_input = st.text_input(
    "Enter topic or website link:"
)

if st.button("Generate Content"):
    with st.spinner("AI agents are working..."):
        if input_type == "Website URL":
            source_text = extract_website_content(user_input)
            result = run_crew(source_text=source_text)
        else:
            result = run_crew(topic=user_input)

    st.success("Content generated successfully!")

    st.markdown("## 📝 Blog Article")
    st.markdown(result["article"])

    st.markdown("## 📘 LinkedIn")
    st.write(result["linkedin"])

    st.markdown("## 📸 Instagram")
    st.write(result["instagram"])

    st.markdown("## 👥 Facebook")
    st.write(result["facebook"])

    pdf_file = generate_pdf(result)
    st.download_button(
        "📥 Download as PDF",
        pdf_file,
        file_name="ai_content_by_akash_bauri.pdf"
    )

    st.markdown("---")
    video_choice = st.radio(
        "Do you want an AI demo video for this content?",
        ["No", "Yes"]
    )

    if video_choice == "Yes":
        with st.spinner("Generating AI demo video..."):
            video_url = generate_ai_video(result["article"])
        st.video(video_url)
