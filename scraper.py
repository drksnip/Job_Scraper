from parser import parse_jobs
from storage import save_to_csv, save_to_sqlite
from filters import filter_jobs
from config import URL, HEADERS, STORAGE_MODE

def main():
    print("🔎 Scraping jobs...")
    jobs = parse_jobs(URL, HEADERS)

    print(f"✅ Scraped {len(jobs)} jobs")

    # Apply filters (example: only jobs in Bangalore, role = Data Analyst)
    filtered_jobs = filter_jobs(jobs, role="Data Analyst", location="Bangalore")

    print(f"✅ {len(filtered_jobs)} jobs after filtering")

    # Save to storage
    if STORAGE_MODE == "csv":
        save_to_csv(filtered_jobs, "output/jobs.csv")
    elif STORAGE_MODE == "sqlite":
        save_to_sqlite(filtered_jobs, "output/jobs.db")

    print("💾 Jobs saved successfully!")

if __name__ == "__main__":
    main()
