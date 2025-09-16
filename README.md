flowchart TD
    A[User Inputs: Resume PDF + Job Description] --> B[Streamlit UI]
    B --> C[PDF Extractor + Text Parser]
    C --> D[LangChain + Gemini API]
    D --> E[AI Skill Gap & ATS Analysis]
    E --> F[Resume Optimization & SWOT Analysis]
    F --> G[Streamlit Output Display]
