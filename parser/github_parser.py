import requests
from github import Github
from typing import List
from api.models import Repository
import os
from dotenv import load_dotenv

load_dotenv()

gh_token = os.getenv('GITHUB_TOKEN')
def get_top_repositories(sort_by: str) -> List[Repository]:
    url = f"https://api.github.com/search/repositories?q=is:public&sort={sort_by}&order=desc"
    response = requests.get(
       url
    )
    data = response.json()["items"][:100]

    repositories = []
    for item in data:
        repository = Repository(
            repo=item["full_name"],
            owner=item["owner"]["login"],
            position_cur=0,
            position_prev=0,
            stars=item["stargazers_count"],
            watchers=item["watchers_count"],
            forks=item["forks_count"],
            open_issues=item["open_issues_count"],
            language=item["language"],
        )
        repositories.append(repository)

    return repositories


def get_repository_activity(owner: str, repo: str) -> dict:
    g = Github(gh_token)
    repository = g.get_repo(f"{owner}/{repo}")

    activity = {
        "date": "2024-03-08",
        "commits": 10,
        "authors": ["author1", "author2"]
    }

    return activity
