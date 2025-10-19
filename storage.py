import csv
import sqlite3

def save_to_csv(jobs, filename):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Job Title", "Company", "Location", "Link"])
        for job in jobs:
            writer.writerow([job["title"], job["company"], job["location"], job["link"]])

def save_to_sqlite(jobs, filename):
    conn = sqlite3.connect(filename)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS jobs 
                 (title TEXT, company TEXT, location TEXT, link TEXT)''')

    c.executemany("INSERT INTO jobs VALUES (:title, :company, :location, :link)", jobs)

    conn.commit()
    conn.close()
