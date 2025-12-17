import streamlit as st
from utils.pdf_generator import generate_pdf

st.set_page_config(page_title="AI Content Creator", layout="wide")

st.title("🤖 AI Professional Content Creator")
st.caption("Developed by Akash Bauri | AI Engineer | Multi-Agent Systems")

# ---------------- INPUT OPTIONS ----------------
input_type = st.radio(
    "Choose content source",
    ["Topic", "Website URL"]
)

user_input = st.text_input(
    "Enter topic or website URL",
    placeholder="e.g. Impact of Dollar on Global Economy OR https://example.com"
)

language = st.selectbox(
    "Select language for content",
    ["English", "Hindi", "Bengali"]
)

generate = st.button("Generate Professional Content")

# ---------------- CONTENT GENERATION ----------------
if generate and user_input:
    if language == "English":
        article = f"""
The global financial system is deeply influenced by the strength and stability
of the United States dollar. As the world’s primary reserve currency, the dollar
plays a crucial role in international trade, investment flows, and monetary policy.

In recent years, fluctuations in the dollar have significantly affected emerging
markets, commodity prices, and inflation rates across the globe. A stronger dollar
often makes imports cheaper while increasing the cost of exports, whereas a weaker
dollar can stimulate exports but add inflationary pressure.

For businesses, investors, and policymakers, understanding the movement of the
dollar is essential for making informed strategic decisions in an interconnected
global economy.
"""

        linkedin = f"""
🔍 Professional Insight: {user_input}

The strength of the US dollar has a direct impact on global markets, trade balances,
and investment strategies. Understanding currency dynamics is no longer optional
for professionals working in finance, business, or policy-making.

🔗 Reference: {user_input}
"""

        instagram = f"""
💡 Market Insight

The US dollar influences everything from fuel prices to global investments.
Staying informed helps you stay ahead.

🔗 Learn more: {user_input}
"""

        facebook = f"""
📊 Let’s talk about the global impact of the US dollar.

Currency movements shape our economy more than we realize — from inflation to
international trade.

🔗 Source: {user_input}
"""

    elif language == "Hindi":
        article = f"""
वैश्विक वित्तीय प्रणाली पर अमेरिकी डॉलर का गहरा प्रभाव पड़ता है।
दुनिया की प्रमुख आरक्षित मुद्रा होने के कारण डॉलर अंतरराष्ट्रीय व्यापार,
निवेश और मौद्रिक नीतियों में महत्वपूर्ण भूमिका निभाता है।

डॉलर में उतार-चढ़ाव उभरते बाजारों, वस्तुओं की कीमतों और महंगाई दरों
को सीधे प्रभावित करता है। इसलिए इसके प्रभाव को समझना आवश्यक है।
"""

        linkedin = f"""
🔍 व्यावसायिक दृष्टिकोण

अमेरिकी डॉलर की मजबूती वैश्विक बाजारों और निवेश निर्णयों को प्रभावित करती है।

🔗 स्रोत: {user_input}
"""

        instagram = f"""
💡 बाजार की जानकारी

डॉलर की स्थिति वैश्विक अर्थव्यवस्था को प्रभावित करती है।

🔗 अधिक जानें: {user_input}
"""

        facebook = f"""
📊 डॉलर और वैश्विक अर्थव्यवस्था

डॉलर का प्रभाव हमारे दैनिक जीवन में स्पष्ट रूप से देखा जा सकता है।

🔗 स्रोत: {user_input}
"""

    else:  # Bengali
        article = f"""
বিশ্ব অর্থনৈতিক ব্যবস্থায় মার্কিন ডলারের প্রভাব অত্যন্ত গুরুত্বপূর্ণ।
বিশ্বের প্রধান রিজার্ভ মুদ্রা হিসেবে ডলার আন্তর্জাতিক বাণিজ্য এবং
বিনিয়োগ সিদ্ধান্তে বড় ভূমিকা পালন করে।

ডলারের ওঠানামা উদীয়মান বাজার, পণ্যের মূল্য এবং মুদ্রাস্ফীতির উপর
সরাসরি প্রভাব ফেলে।
"""

        linkedin = f"""
🔍 পেশাদার বিশ্লেষণ

মার্কিন ডলারের শক্তি বৈশ্বিক বাজার এবং বিনিয়োগ কৌশলকে প্রভাবিত করে।

🔗 উৎস: {user_input}
"""

        instagram = f"""
💡 বাজার আপডেট

ডলার বিশ্ব অর্থনীতির গুরুত্বপূর্ণ চালিকা শক্তি।

🔗 আরও জানুন: {user_input}
"""

        facebook = f"""
📊 ডলার ও বিশ্ব অর্থনীতি

ডলারের পরিবর্তন আমাদের দৈনন্দিন জীবনে প্রভাব ফেলে।

🔗 উৎস: {user_input}
"""

    # ---------------- DISPLAY ----------------
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
        reference_link=user_input,
        language=language
    )

    st.download_button(
        label="📥 Download Professional PDF",
        data=pdf_bytes,
        file_name="AI_Professional_Content_Report.pdf",
        mime="application/pdf"
    )
