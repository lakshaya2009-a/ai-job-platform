import re

def extract_skills(resume_text):
    skills = ["python", "java", "sql", "machine learning", "excel"]
    
    found_skills = []
    
    for skill in skills:
        if re.search(skill, resume_text.lower()):
            found_skills.append(skill)
    
    return found_skills