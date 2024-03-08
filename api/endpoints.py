from fastapi import APIRouter, Query
from typing import List
from .models import Repository
from parser import github_parser

app = APIRouter()

@app.get("/api/repos/top100")
async def get_top_repositories(sort_by: str = Query("stars")) -> List[Repository]:
    repositories = github_parser.get_top_repositories(sort_by)
    return repositories

@app.get("/api/repos/{owner}/{repo}/activity")
async def get_repository_activity(owner: str, repo: str) -> dict:
    activity = github_parser.get_repository_activity(owner, repo)
    return activity
