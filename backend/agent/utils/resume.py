import re

def extract_skills(resume_text):
    skills = ["python", "java", "sql", "machine learning", "excel"]
    
    found_skills = []
    
    for skill in skills:
        if re.search(skill, resume_text.lower()):
            found_skills.append(skill)
    
    return found_skills
import pdfplumber

def extract_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text