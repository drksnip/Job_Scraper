def filter_jobs(jobs, role=None, location=None):
    filtered = []

    for job in jobs:
        if role and role.lower() not in job["title"].lower():
            continue
        if location and location.lower() not in job["location"].lower():
            continue
        filtered.append(job)

    return filtered
