import sys
import os

# Ensure root directory is available for imports (Streamlit Cloud safe)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st

from helper import load_env
load_env()

from utils.pdf_generator import generate_pdf
from utils.web_scraper import extract_website_content

# ---------------- UI CONFIG ----------------
st.set_page_config(
    page_title="AI Content Creator",
    page_icon="🤖",
    layout="wide"
)

st.sidebar.markdown("""
### 🤖 AI Content Creator  
**Developed by Akash Bauri**  
AI Engineer | Multi-Agent Systems | LLM Automation
""")

st.title("AI Autonomous Content Creator & Repurposing Platform 🚀")

# ---------------- USER INPUT ----------------
input_type = st.radio(
    "Choose input type:",
    ["Topic", "Website URL"]
)

user_input = st.text_input(
    "Enter topic or website link:"
)

# ---------------- ACTION ----------------
if st.button("Generate Content"):
    if not user_input:
        st.warning("Please enter a topic or website URL.")
    else:
        with st.spinner("AI is generating content..."):
            if input_type == "Website URL":
                source_text = extract_website_content(user_input)
                article = f"Generated content based on website:\n\n{source_text[:2000]}"
            else:
                article = f"Generated content for topic:\n\n{user_input}"

        st.success("Content generated successfully!")

        # ---------------- OUTPUT ----------------
        st.markdown("## 📝 Blog Article")
        st.markdown(article)

        st.markdown("## 💼 LinkedIn Post")
        linkedin = f"🔍 Insights on {user_input}\n\n#AI #Automation #Content"
        st.write(linkedin)

        st.markdown("## 📸 Instagram Post")
        instagram = f"{user_input}\n✨ #AI #Tech #Innovation"
        st.write(instagram)

        st.markdown("## 👥 Facebook Post")
        facebook = f"Let’s talk about {user_input} and its impact!"
        st.write(facebook)

        # ---------------- PDF DOWNLOAD ----------------
        pdf_bytes = generate_pdf({
            "Article": article,
            "LinkedIn": linkedin,
            "Instagram": instagram,
            "Facebook": facebook
        })

        st.download_button(
            label="📥 Download as PDF",
            data=pdf_bytes,
            file_name="ai_content_by_akash_bauri.pdf",
            mime="application/pdf"
        )
