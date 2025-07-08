import google.generativeai as genai
import streamlit as st
from utils import extract_text_from_pdf,fetch_job_description
resume_text=extract_text_from_pdf
jd_text=fetch_job_description
# Initialize the GenAI client
api_key=st.secrets['gemini_api_key']
client = genai.configure(api_key)
model = genai.GenerativeModel("gemma-3-27b-it")
# Input prompt from the user (e.g., paste resume or job description)
#job_description = input("\nPaste the job description you’re applying to:\n")

# Structured input template for ATS Checker
def analyze_resume_with_jd(resume_text: str, jd_text: str) -> str:
    """Returns AI-generated ATS feedback."""
    prompt_template = f"""
    You are an ATS (Applicant Tracking System) expert.

    Evaluate how well the following resume matches the job description.

    Resume:
    {resume_text}

    Job Description:
    {jd_text}

   Provide (plain text only):
    1. A compatibility score out of 100.
    2. Key missing keywords or skills from the resume.
    3. Suggestions to improve resume for this job.
    4. One-line feedback summary.
    """
    try:
        response = model.generate_content(prompt_template)
        return response.text
    except Exception as e:
        return f"❌ Error generating response: {e}"
