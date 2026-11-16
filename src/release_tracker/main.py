from datetime import UTC, datetime

from fastapi import FastAPI, HTTPException, status

from .models.project import ProjectRead

app = FastAPI(title="Release Tracker API")

_seed_time = datetime(2026, 1, 1, tzinfo=UTC)


@app.get('/projects/{p_id}', response_model=ProjectRead)
def get_project(p_id: int):
    project = mock_db.get(p_id)

    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    return project

@app.get("/projects")
def list_projects(slug: str | None = None):
    projects = list(mock_db.values())

    if slug is None:
        return projects

    return [project for project in projects if project.slug == slug]

mock_db: dict[int, ProjectRead] = {
    1: ProjectRead(id=1, title="Frontend Restyle", slug="frontend-restyle", created_at=_seed_time),
    2: ProjectRead(id=2, title="API v2", slug="api-v2", created_at=_seed_time),
    3: ProjectRead(id=3, title="DB Migration", slug="db-migration", created_at=_seed_time)
}
