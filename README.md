📄 SkillMatch - AI Assisted Job Matching Tool

SkillMatch is an AI-powered resume optimization and job-matching assistant built using Streamlit and Google Gemini.
It analyzes resumes against job descriptions, identifies skill gaps, predicts ATS scores, and generates tailored resume recommendations.

🌐 Live App: skill-match.streamlit.app

💻 GitHub: SkillMatch Repository

🚀 Features

📂 Upload Resume (PDF) & Job Description

🤖 AI-powered skill gap analysis

📊 ATS score prediction & matching insights

💡 Resume improvement recommendations

📑 Auto-generated customized resumes (ATS-friendly)

📝 One-page copy-paste ready resume format

📌 SWOT analysis for better self-assessment

🎯 Target Users

Job seekers struggling to tailor resumes for multiple job descriptions

Students preparing for placements

Recruiters/HR teams looking to streamline shortlisting

Career portals and consultancies offering resume services

🛠️ Tech Stack

Frontend: Streamlit (Python)

Backend: Google Gemini 2.5 Flash Lite API + LangChain

Libraries:

streamlit

google-generativeai

langchain_google_genai

pandas, dotenv, requests

Deployment: Streamlit Cloud

🏗️ Architecture
flowchart TD
    A[User Inputs: Resume PDF + Job Description] --> B[Streamlit UI]
    B --> C[PDF Extractor + Text Parser]
    C --> D[LangChain + Gemini API]
    D --> E[AI Skill Gap & ATS Analysis]
    E --> F[Resume Optimization & SWOT]
    F --> G[Streamlit Output Display]
