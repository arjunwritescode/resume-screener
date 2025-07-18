# File: main.py

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import fitz  # PyMuPDF
import os
import openai
from typing import List
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TARGET_SKILLS = ["Python", "React", "Node.js", "SQL", "Machine Learning", "FastAPI", "Docker"]

def extract_text_from_pdf(pdf_bytes) -> str:
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def basic_score_resume(resume_text: str, target_skills: List[str]) -> dict:
    score = 0
    matched_skills = []
    for skill in target_skills:
        if skill.lower() in resume_text.lower():
            score += 1
            matched_skills.append(skill)
    return {"score": score, "matched_skills": matched_skills, "total_skills": len(target_skills)}

async def openai_score_resume(resume_text: str) -> dict:
    prompt = (
        "You are an AI recruiter. Score this resume out of 10 for a software development role. "
        "Mention key skills detected and give a short verdict:\n\n" + resume_text
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You evaluate resumes."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
        )
        return {"verdict": response.choices[0].message.content}
    except Exception as e:
        return {"error": str(e)}

@app.post("/upload_resume/")
async def upload_resume(file: UploadFile = File(...)):
    contents = await file.read()
    resume_text = extract_text_from_pdf(contents)
    basic_score = basic_score_resume(resume_text, TARGET_SKILLS)
    ai_score = await openai_score_resume(resume_text)
    return {
        "filename": file.filename,
        "basic_score": basic_score,
        "ai_score": ai_score,
        "resume_text_excerpt": resume_text[:500]
    }
