import requests
from bs4 import BeautifulSoup

def parse_jobs(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("❌ Failed to fetch page:", response.status_code)
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    job_cards = soup.find_all("div", class_="job-card")  # change for actual site
    jobs = []

    for card in job_cards:
        try:
            title = card.find("h2", class_="title").get_text(strip=True)
            company = card.find("div", class_="company").get_text(strip=True)
            location = card.find("span", class_="location").get_text(strip=True)
          # link = card.find("a", href=True)["href"]

            jobs.append({
                "title": title,
                "company": company,
                "location": location,
                #link": link
            })
        except AttributeError:
            continue  # skip if any field is missing

    return jobs
