# 🤖 AI Autonomous Content Creator & Repurposing Platform

**Developed by Akash Bauri**  
*AI Engineer | Multi-Agent Systems | LLM Automation*

---

## 📌 Project Overview

The **AI Autonomous Content Creator & Repurposing Platform** is a production-ready AI application that autonomously generates high-quality content using a **multi-agent AI system**.

The platform allows users to input either:
- A **topic**, or
- A **website URL**

The system then:
- Analyzes real-world content
- Generates a **long-form blog article**
- Repurposes the content into **platform-specific social media posts**
- Allows users to **download the complete output as a PDF**
- Optionally generates an **AI demo video**, only after explicit user consent

This project is designed to be **fully deployable on Streamlit Cloud** and demonstrates **real-world AI product engineering practices**.

---

## 🎯 Key Objectives

- Build a **real-world AI content automation system**
- Demonstrate **multi-agent collaboration**
- Show **LLM orchestration and tool usage**
- Deliver **structured, business-ready outputs**
- Ensure **ethical AI usage** (consent-based video generation)
- Deploy using **cloud-friendly architecture**

---

User Input (Topic / Website URL)
↓
Web Scraper & Content Extractor
↓
Market Analysis Agent
↓
Content Creation Agent
↓
Quality Assurance Agent
↓
Categorized Output (Blog + Social Media)
↓
PDF Export / Optional AI Video


Each agent performs a **specialized role**, simulating a real content team workflow.

---

## 🧩 Features

### 🔹 Input Options
- Topic-based content generation
- Website URL-based content repurposing

### 🔹 AI-Generated Outputs
- 📝 Blog Article (Markdown)
- 💼 LinkedIn Post (Professional tone)
- 📸 Instagram Post (Engaging, short-form)
- 👥 Facebook Post (Conversational style)

### 🔹 Downloadable Content
- One-click **PDF download**
- Structured, share-ready format
- Includes author credit

### 🔹 Optional AI Video Demo
- AI explainer video generated **only after user approval**
- Uses external video generation APIs
- Fully compatible with Streamlit Cloud

### 🔹 Deployment Ready
- GitHub-based deployment
- Secure API keys via Streamlit Secrets
- Cloud-safe execution

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---------|--------|
| Python | Core programming |
| Streamlit | Web interface & deployment |
| CrewAI | Multi-agent orchestration |
| Groq (LLaMA 3.3 – 70B) | Large Language Model |
| Pydantic | Structured AI outputs |
| Serper API | Real-time web search |
| BeautifulSoup | Website content extraction |
| YAML | Agent & task configuration |
| FPDF | PDF generation |
| GitHub | Version control |

---

## 📂 Project Structure

ai-content-creator/
│
├── app.py # Main Streamlit application
├── helper.py # Environment loader
├── requirements.txt
├── README.md
│
├── config/
│ ├── agents.yaml # Agent definitions
│ └── tasks.yaml # Task workflows
│
├── utils/
│ ├── pdf_generator.py # PDF creation logic
│ ├── web_scraper.py # Website content extraction
│ └── video_generator.py # Optional AI video integration
│
├── .streamlit/
│ └── secrets.toml # Secure API keys
│
└── assets/
└── styles.css


---

## 👤 How Users Interact With the App

1. Open the Streamlit application
2. Choose input type:
   - Topic
   - Website URL
3. Enter the topic or paste the link
4. Click **Generate Content**
5. View categorized AI outputs
6. Download the content as a PDF
7. (Optional) Confirm to generate an AI demo video

---

## 🔐 Security & Ethics

- API keys are stored securely using **Streamlit Secrets**
- Website content is **analyzed and rewritten**, not copied
- AI video generation requires **explicit user consent**
- No personal data is stored or tracked

---

## 🚀 Deployment (Streamlit Cloud)

1. Push the project to GitHub
2. Log in to **Streamlit Cloud**
3. Connect your GitHub repository
4. Set API keys in **Streamlit → App Secrets**
5. Deploy

The application runs entirely in the cloud with no local setup required.

---

## 📄 Resume-Ready Description

> Developed a multi-agent AI content creation platform using CrewAI and Groq LLaMA 3.3. The system autonomously analyzes topics or website content, generates long-form articles, repurposes content for multiple social media platforms, and delivers structured outputs with PDF export support. Designed with production-grade architecture and deployed on Streamlit Cloud.

---

## 🌟 Why This Project Matters

This project demonstrates:
- Real-world **AI system design**
- Multi-agent collaboration
- Product-level thinking
- Cloud deployment skills
- Ethical AI practices

It is suitable for roles such as:
- AI Engineer
- AI Product Engineer
- Applied ML Engineer
- LLM Engineer
- Automation Engineer

---

## 👨‍💻 Author

**Akash Bauri**  
AI Engineer | Multi-Agent Systems | LLM Automation  

---


## 🧠 System Architecture

