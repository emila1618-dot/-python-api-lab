
import json
from pathlib import Path
import requests
from datetime import datetime, timezone
# API 1 - GitHub
github_url = "https://api.github.com/repos/python/cpython"

# API 2 - aktualna godzina
time_url = "https://worldtimeapi.org/api/timezone/Etc/UTC"


import requests

def get_data(url):
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print(f"Błąd połączenia z {url}: {error}")
        return None


def main():
    github = get_data(github_url)
    clock = {"datetime": datetime.now(timezone.utc).isoformat()}
    if github is None or clock is None:
        print("Nie udało się pobrać danych z API.")
        return
    report = {
        "project": github["full_name"],
        "description": github["description"],
        "stars": github["stargazers_count"],
        "last_push": github["pushed_at"],
        "checked_at": clock["datetime"],
        "source": github["html_url"]
    }

    Path("report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    print("Raport utworzony!")
    print(json.dumps(report, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
