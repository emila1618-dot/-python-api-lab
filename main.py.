
import json
from pathlib import Path
import requests

# API 1 - GitHub
github_url = "https://api.github.com/repos/python/cpython"

# API 2 - aktualna godzina
time_url = "https://worldtimeapi.org/api/timezone/Etc/UTC"

def get_data(url):
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    return response.json()

def main():
    github = get_data(github_url)
    clock = get_data(time_url)

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
