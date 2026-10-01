# AI Resume Analyzer

A Streamlit web app that analyzes resumes using Gemini AI and gives actionable feedback for specific job roles.

## Features

- Upload resumes in **PDF** or **DOCX** format
- Paste resume text directly
- Choose a target role (AI/ML, Data Science, Full Stack, etc.)
- Get AI-powered analysis including:
  - Skills found
  - Missing critical skills
  - Suitable roles
  - ATS score
  - Improvement suggestions
  - Overall rating
- Download the generated analysis as a text file

## Tech Stack

- [Streamlit](https://streamlit.io/)
- [Google GenAI Python SDK](https://pypi.org/project/google-genai/)
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [python-docx](https://pypi.org/project/python-docx/)

## Prerequisites

- Python 3.9+
- A valid Gemini API key

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/pkpranesh/Resume-Analyzer.git
   cd Resume-Analyzer
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Set your Gemini API key as an environment variable:

```bash
export GEMINI_API_KEY="your_api_key_here"
```

> If `GEMINI_API_KEY` is not set, the app falls back to a placeholder value and API calls will fail.

## Run the App

```bash
streamlit run app.py
```

Then open the local URL shown in your terminal (usually `http://localhost:8501`).

## Usage

1. Select your target job role.
2. Upload a resume file or paste resume text.
3. Click **Analyze Resume**.
4. Review the generated feedback and optionally download it.

## Project Structure

```text
Resume-Analyzer/
├── app.py
├── requirements.txt
└── README.md
```

## Notes

- Use text-based PDFs for better extraction accuracy.
- Very large resumes may produce slower responses due to model processing time.
