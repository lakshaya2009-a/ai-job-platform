from utils.resume_parser import extract_skills
from utils.job_fetcher import load_jobs
from agents.job_matcher import match_jobs

resume_text = input("Paste your resume text: ")

skills = extract_skills(resume_text)
jobs = load_jobs()

matched = match_jobs(skills, jobs)

print("\nTop Job Matches:\n")

for job in matched:
    print(f"{job['title']} - Score: {job['score']}")