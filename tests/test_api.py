import sys
import os

# Add the root folder of the project to Python's search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import create_app
from app.database import mongo

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["MONGO_URI"] = "mongodb://localhost:27017/test_todo_db"
    with app.test_client() as client:
        with app.app_context():
            mongo.db.todos.drop()  # Clear test database before each run
        yield client

def test_add_todo(client):
    response = client.post('/api/todos', json={"title": "Test Todo", "description": "Test Description"})
    assert response.status_code == 201

def test_get_todos(client):
    client.post('/api/todos', json={"title": "Test Todo", "description": "Test Description"})
    response = client.get('/api/todos')
    print(response.json)
    assert response.status_code == 200
    assert len(response.get_json()) > 0

def test_delete_todo(client):
    response = client.post('/api/todos', json={"title": "Test Todo", "description": "Test Description"})
    todo_id = response.get_json()["id"]
    delete_response = client.delete(f'/api/todos/{todo_id}')
    assert delete_response.status_code == 200
