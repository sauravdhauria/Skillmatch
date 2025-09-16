import streamlit as st
from pdf_extractor import text_extractor
import google.generativeai as genai
import os

# configure the model

key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-2.5-flash-lite")
resume_text = job_desc =None

#upload resume

st.sidebar.title(":blue[UPLOAD YOUR RESUME(PDF ONLY)]")

#lets read the pdf file and extract text
file=st.sidebar.file_uploader('Resume', type=['pdf'])
if file:
    resume_text=text_extractor(file)


    #st.write(resume_text) 


#Lets define the main page: 

st.title(":orange[SKILLMATCH] : :blue[AI ASSISTED JOB MATCHING TOOL]")
st.markdown("##### :green[Find your perfect job match with SkillMatch - The AI-powered job matching tool that connects your skills to top job opportunities!]")
tips='''Follow these steps to proceed:
* Upload your resume in the sidebar (PDF format only)
* Copy and paste the job description below for which you are applying
* Click the button and see the magic.'''
st.write(tips)

job_desc=st.text_area("Copy and Paste the Job Description here",max_chars=10000)

promt=f'''Assume you are and expert in skill matching and creating profiles
Match the following resume with the job description provided by the user.
resume: {resume_text}
job description: {job_desc}

* Give a brief description of applicant in 3 to 5 lines.
* Give a range expected ATS score along with matching and non matching skills in bullet points.
* Give the chances of getting shortlisted for the position in percentage.
* Perform SWOT analysis and discuss each and everything in bullet points.
* Suggest what all improvements cab be made in resume in order get better ATS and increase the chances of getting shortlisted.
* Also create two customized resume as per the job description provided to get better ATS and increase the chances of getting shortlisted.
* Preare a one page resume in such a format that can be copied and pasted in word.
* Use bullet points and tables wherever required.'''

button=st.button("Clicks")
if button:
    if resume_text and job_desc:
        response=model.generate_content(promt)
        st.write(response.text)
    else:
        st.write("Please upload your resume and job description to proceed.")
   
    


