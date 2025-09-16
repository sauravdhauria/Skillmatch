# 📄 SkillMatch - AI Assisted Job Matching Tool

SkillMatch is an AI-powered resume optimization and job-matching assistant built using Streamlit and Google Gemini.
It analyzes resumes against job descriptions, identifies skill gaps, predicts ATS scores, and generates tailored resume recommendations.

 🌐 Live App: skillmatchaisaurav.streamlit.app

---

## 🚀 Features
- 📂 Upload resume (PDF) & job description  
- 🤖 AI-powered skill gap analysis & ATS score prediction  
- 📊 Matching and non-matching skills breakdown 
- 💡 Resume improvement recommendations  
- 📝 Auto-generated ATS-friendly customized resumes  
- 📌 SWOT analysis for better self-assessment
---

## 🎯 Target Users
- Job seekers applying for multiple roles
- Students preparing for campus placements
- Recruiters & HR teams shortlisting resumes
- Career portals and consultancies offering resume services
---

## 🛠️ Tech Stack
- Frontend: Streamlit (Python)  
- Backend: Google Gemini 2.5 Flash Lite API  
- Libraries:  
  - `streamlit`  
  - `pandas`  
  - `google-generativeai`  
  - `dotenv`, `requests`, `langchain_google_genai`  

---

## 🏗️ Architecture
```mermaid
flowchart TD
    A[User Inputs: Resume PDF + Job Description] --> B[Streamlit UI]
    B --> C[PDF Extractor + Text Parser]
    C --> D[LangChain + Gemini API]
    D --> E[AI Skill Gap & ATS Analysis]
    E --> F[Resume Optimization & SWOT Analysis]
    F --> G[Streamlit Output Display]
