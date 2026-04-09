def match_jobs(user_skills, jobs):
    matched_jobs = []

    for job in jobs:
        match_score = len(set(user_skills) & set(job["skills"]))
        
        if match_score > 0:
            job["score"] = match_score
            matched_jobs.append(job)

    matched_jobs.sort(key=lambda x: x["score"], reverse=True)
    
    return matched_jobs