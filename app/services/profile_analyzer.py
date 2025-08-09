





from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from typing import List
import re
import os

# Custom skill keywords (expandable)
KNOWN_SKILLS = [
    "Python", "SQL", "Java", "C++", "Machine Learning", "Deep Learning", 
    "AI", "Leadership", "Data Analysis", "NLP", "Cloud", "AWS", "Docker"
]

def clean_text(text: str) -> str:
    # Remove non-alphabetic characters and extra whitespace
    return re.sub(r'\s+', ' ', re.sub(r'[^A-Za-z0-9\s]', '', text)).strip()

def extract_skills(text: str, skill_keywords: List[str]) -> List[str]:
    found = []
    for keyword in skill_keywords:
        if re.search(rf"\b{re.escape(keyword)}\b", text, flags=re.IGNORECASE):
            found.append(keyword)
    return list(set(found))

def analyze_resume(pdf_path: str) -> dict:
    if not os.path.exists(pdf_path):
        return {"error": "File does not exist."}

    try:
        reader = PdfReader(pdf_path)
        text = " ".join([page.extract_text() or "" for page in reader.pages])
        text = clean_text(text)

        skills = extract_skills(text, KNOWN_SKILLS)

        # Simple inference
        industry = "IT / AI" if any(skill in skills for skill in ["AI", "Machine Learning", "Python"]) else "General Tech"
        interests = ["Tech", "Innovation"] if "Python" in skills else ["Development"]

        return {
            "skills": skills,
            "industry": f"Likely: {industry}",
            "interests": interests,
        }
    except Exception as e:
        return {"error": str(e)}
