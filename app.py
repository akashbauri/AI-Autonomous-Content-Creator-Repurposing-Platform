import streamlit as st
from utils.pdf_generator import generate_pdf

st.set_page_config(page_title="AI Content Creator", layout="wide")

st.title("🤖 AI Content Creator & Repurposing Platform")
st.caption("Developed by Akash Bauri | AI Engineer | Multi-Agent Systems")

# ---- INPUT ----
topic = st.text_input("Enter your topic", "Dollar and its impact")

# ---- MOCK CONTENT (replace with LLM later if needed) ----
article = f"""
The dollar plays a crucial role in the global economy.
Its fluctuations impact trade, inflation, and emerging markets.
"""

linkedin = f"""
📌 {topic}

The dollar has a major influence on global markets.
Understanding its movement helps professionals make better decisions.
"""

instagram = f"""
💸 {topic}

The dollar affects everything from fuel prices to tech stocks.
Stay informed. 📈
"""

facebook = f"""
Let’s talk about {topic}!

The dollar’s strength or weakness impacts daily life more than we realize.
"""

# ---- DISPLAY ----
st.subheader("📝 Generated Content")
st.write("### Article")
st.write(article)

st.write("### LinkedIn")
st.write(linkedin)

st.write("### Instagram")
st.write(instagram)

st.write("### Facebook")
st.write(facebook)

# ---- PDF GENERATION ----
pdf_buffer = generate_pdf({
    "Article": article,
    "LinkedIn Post": linkedin,
    "Instagram Caption": instagram,
    "Facebook Post": facebook
})

# ---- DOWNLOAD ----
st.download_button(
    label="📥 Download as PDF",
    data=pdf_buffer,
    file_name="AI_Content_Report.pdf",
    mime="application/pdf"
)
