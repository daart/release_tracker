from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Release Tracker")


class ProjectRead(BaseModel):
    id: int
    title: str
    slug: str





@app.get('/projects/{p_id}', response_model=ProjectRead)
def get_project(p_id: int):
    return mock_db.get(p_id)

@app.get("/projects")
def list_projects(title: str | None = None):
    filtered = list(mock_db.values())
    if title is None:
        return filtered

    return [p for p in filtered if p.title == title]


mock_db: dict[int, ProjectRead] = {
    1: ProjectRead(id=1, title="Frontend Restyle", slug="frontend-restyle"),
    2: ProjectRead(id=2, title="API v2", slug="api-v2"),
    3: ProjectRead(id=3, title="DB Migration", slug="db-migration")
}
