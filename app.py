import streamlit as st
from utils import extract_text_from_pdf, fetch_job_description
from ai import analyze_resume_with_jd

# --- Page Setup ---
st.set_page_config(page_title="ATS Resume & JD Analyzer")
st.markdown("<h1 class='main-title'>📄 ATS Resume & Job Description Analyzer</h1>", unsafe_allow_html=True)

# --- Custom Dark Theme CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&display=swap');

body, .stApp {
    font-family: 'Space Grotesk', sans-serif;
    background: linear-gradient(to bottom right, #1f1f2e, #2a2a40);
    color: #e0e0e0;
}

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.main-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(1.5rem, 5vw, 2.5rem)
    font-weight: 700;
    color: #ffffff;
    white-space: nowrap;
    text-align: center;
    margin-bottom: 2rem;
    text-shadow: 0 1px 2px rgba(0,0,0,0.5);
}
            
@media (max-width: 900px) {
    .main-title {
        font-size: 1.5rem !important;
    }
}

/* Small screens (phones) */
@media (max-width: 600px) {
    .main-title {
        font-size: 1.1rem !important;
    }
}



div.stButton > button:first-child {
    background: linear-gradient(135deg, #3a58e0, #658bf5);
    color: white;
    padding: 0.6rem 1.4rem;
    border: none;
    border-radius: 12px;
    font-size: 16px;
    font-weight: 600;
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
}

div.stButton > button:first-child:hover {
    background: linear-gradient(135deg, #2e49c0, #5e84e0);
    transform: scale(1.02);
}

textarea, .stTextInput > div > input, .stFileUploader > div {
    background: #1e1e2e !important;
    border-radius: 12px !important;
    border: 1px solid #3c3f4f !important;
    box-shadow: 0 2px 6px rgba(0,0,0,0.3);
    padding: 10px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 15px;
    color: #e0e0e0;
}

h1, .stTitle {
    font-size: 2.5rem !important;
    color: #ffffff !important;
    font-weight: 700 !important;
    text-shadow: 0px 1px 2px rgba(0,0,0,0.3);
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# --- Resume Upload ---
uploaded_file = st.file_uploader("📤 Upload your PDF resume", type=["pdf"])

# --- Job Description Input ---
job_desc_input = st.text_area("📝 Paste the Job Description")

resume_text = ""
jd_text = ""

if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)
    st.success("✅ Resume extracted!")

if job_desc_input:
    jd_text = fetch_job_description(job_desc_input)
    st.success("✅ Job description received!")
# --- Analyze Button ---
analyze_clicked = st.button("🔍 Analyze with ATS Checker")

if analyze_clicked:
    if not uploaded_file or not job_desc_input:
        st.warning("⚠️ Please upload your resume and paste a job description to begin analysis.")
    else:
        with st.spinner("Analyzing resume and JD with Gemini..."):
            response = analyze_resume_with_jd(resume_text, jd_text)
            with st.expander("📄 View Full Report"):
                st.markdown(response)
else:
    st.info("📎 Upload your resume and paste a job description to begin analysis.")
