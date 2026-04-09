import json

def load_jobs():
    with open("data/sample_jobs.json", "r") as f:
        jobs = json.load(f)
    return jobs