from fastapi.testclient import TestClient

from release_tracker.main import app

client = TestClient(app)

def test_list_projects():
    res = client.get("/projects")

    assert res.status_code == 200

    
