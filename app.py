import streamlit as st
from google import genai
import PyPDF2
import docx
import io
import os

# ── Page Config ───────────────────────────────────────────
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# ── Gemini Setup ──────────────────────────────────────────
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY", "YOUR_API_KEY_HERE"))

# ── Helper Functions ──────────────────────────────────────
def extract_pdf_text(file):
    reader = PyPDF2.PdfReader(file)
    return " ".join(page.extract_text() for page in reader.pages)

def extract_docx_text(file):
    doc = docx.Document(file)
    return " ".join(para.text for para in doc.paragraphs)

def analyze_resume(resume_text, job_role="AI/ML Engineer"):
    prompt = f"""
    You are an expert technical recruiter specializing in {job_role} roles.
    
    Analyze this resume and provide:
    
    1. **Skills Found** — List all technical and soft skills
    2. **Missing Skills** — Critical skills missing for {job_role} roles
    3. **Suitable Roles** — Top 5 roles this person can apply for RIGHT NOW
    4. **ATS Score** — Rate resume ATS compatibility out of 10
    5. **Improvements** — Top 5 specific actionable improvements
    6. **Overall Rating** — Rate this resume out of 10 with justification
    
    Resume:
    {resume_text}
    
    Be specific, actionable, and honest.
    """
    
    response = client.models.generate_content(
        model   = 'gemini-3.8-flash',
        contents = prompt
    )
    return response.text

# ── UI ────────────────────────────────────────────────────
st.title("📄 AI Resume Analyzer")
st.markdown("### Get instant AI-powered feedback on your resume")
st.markdown("---")

# Job role selector
job_role = st.selectbox(
    "Target Role:",
    ["AI/ML Engineer", "Data Scientist", "Full Stack Developer",
     "Backend Developer", "Frontend Developer", "MLOps Engineer",
     "LLM Engineer", "GenAI Developer"]
)

st.markdown("---")

# Two input methods
tab1, tab2 = st.tabs(["📤 Upload Resume", "✍️ Paste Text"])

resume_text = ""

with tab1:
    uploaded_file = st.file_uploader(
        "Upload your resume (PDF or DOCX)",
        type=['pdf', 'docx']
    )
    if uploaded_file:
        if uploaded_file.name.endswith('.pdf'):
            resume_text = extract_pdf_text(uploaded_file)
        else:
            resume_text = extract_docx_text(uploaded_file)
        st.success(f"✅ File uploaded: {uploaded_file.name}")
        with st.expander("Preview extracted text"):
            st.write(resume_text[:500] + "...")

with tab2:
    resume_text = st.text_area(
        "Paste your resume text here:",
        height=300,
        placeholder="Paste your resume content..."
    )

st.markdown("---")

# Analyze button
if st.button("🔍 Analyze Resume", type="primary", use_container_width=True):
    if not resume_text.strip():
        st.error("Please upload a resume or paste your text first!")
    else:
        with st.spinner("🤖 Gemini is analyzing your resume..."):
            result = analyze_resume(resume_text, job_role)

        st.markdown("## 📊 Analysis Results")
        st.markdown(result)

        # Download results
        st.download_button(
            label     = "📥 Download Analysis",
            data      = result,
            file_name = "resume_analysis.txt",
            mime      = "text/plain"
        )

# ── Sidebar ───────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 💡 Tips for Best Results")
    st.info(
        "→ Use a clean, text-based PDF\n"
        "→ Include all skills explicitly\n"
        "→ Add metrics to projects\n"
        "→ Include live project URLs"
    )
    st.markdown("---")
    st.markdown("**Built by Pranesh P K**")
    st.markdown("SRM IST | B.Tech ECE | 2026")

# ── Footer ────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:gray;'>"
    "AI Resume Analyzer | Powered by Gemini AI | Built by Pranesh P K"
    "</p>",
    unsafe_allow_html=True
)
