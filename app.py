import streamlit as st
from utils.pdf_generator import generate_pdf

st.set_page_config(page_title="AI Content Creator", layout="wide")

st.title("🤖 AI Professional Content Creator")
st.caption("Developed by Akash Bauri | AI Engineer | LLM Automation")

# ---------------- INPUT ----------------
topic_or_url = st.text_input(
    "Enter topic or website URL",
    placeholder="e.g. AI Technology or https://example.com",
)

language = st.selectbox(
    "Select language for content",
    ["English", "Hindi", "Bengali"]
)

generate = st.button("Generate Professional Content")

# ---------------- LOGIC ----------------
if generate and topic_or_url:

    # ✅ Dynamic professional content
    article = f"""
{topic_or_url} is rapidly shaping the modern digital landscape.

In today’s interconnected world, this topic plays a critical role in driving
innovation, productivity, and long-term economic growth. Organizations across
industries are leveraging advancements in this domain to remain competitive
and future-ready.

From business leaders to policymakers, understanding the implications of
{topic_or_url} is essential for making informed strategic decisions in a
technology-driven global economy.
"""

    linkedin = f"""
🔍 Professional Insight: {topic_or_url}

This topic is transforming industries by enabling smarter decisions,
automation, and scalable innovation.

Professionals who stay informed gain a strategic advantage in an
ever-evolving digital ecosystem.
"""

    instagram = f"""
💡 {topic_or_url}

Innovation begins with awareness.
Understanding trends today prepares us for opportunities tomorrow.
"""

    facebook = f"""
📊 Let’s talk about {topic_or_url}

This subject is reshaping how we work, communicate, and innovate.
Staying informed is the first step toward growth.
"""

    # ---------------- UI ----------------
    st.subheader("📝 Professional Blog Article")
    st.write(article)

    st.subheader("💼 LinkedIn Post")
    st.write(linkedin)

    st.subheader("📸 Instagram Caption")
    st.write(instagram)

    st.subheader("👥 Facebook Post")
    st.write(facebook)

    # ---------------- PDF ----------------
    pdf_bytes = generate_pdf(
        content={
            "Professional Blog Article": article,
            "LinkedIn Post": linkedin,
            "Instagram Caption": instagram,
            "Facebook Post": facebook,
        },
        reference_link=topic_or_url,
        language=language,
    )

    # ✅ CRITICAL FIX
    if pdf_bytes and isinstance(pdf_bytes, (bytes, bytearray)):
        st.download_button(
            label="📥 Download Professional PDF",
            data=pdf_bytes,
            file_name="AI_Professional_Content_Report.pdf",
            mime="application/pdf",
        )
    else:
        st.error("PDF generation failed. Please try again.")
