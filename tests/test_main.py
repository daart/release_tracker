from fastapi.testclient import TestClient

from release_tracker.main import app

client = TestClient(app)

def test_list_projects():
    res = client.get("/projects")

    assert res.status_code == 200

def list_projects_by_slug():
    res = client.get('/projects', params={"slug": "api-v2"})
    assert res.status_code == 200
    data = res.json()
    assert data[0]["slug"] == "api-v2"

def test_get_project():
    res = client.get('/projects/1')
    assert res.status_code == 200
    assert res.json()["title"] == "Frontend Restyle"

def test_get_project_not_found():
    res = client.get('/projects/999')
    assert res.status_code == 404
    assert res.json()["detail"] == "Project not found"