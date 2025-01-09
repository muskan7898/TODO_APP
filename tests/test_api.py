import sys
import os

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
            mongo.db.todos.drop() 
        yield client

''' 
Test case for adding a new todo
'''
def test_add_todo(client):
    response = client.post('/api/todos', json={"title": "Test Todo", "description": "Test Description"})
    assert response.status_code == 201


'''
Test case for getting all todos
'''

def test_get_todos(client):
    client.post('/api/todos', json={"title": "Test Todo", "description": "Test Description"})
    response = client.get('/api/todos')
    print(response.json)
    assert response.status_code == 200
    assert len(response.get_json()) > 0


''' Test case for delte todo '''

def test_delete_todo(client):
    response = client.post('/api/todos', json={"title": "Test Todo", "description": "Test Description"})
    todo_id = response.get_json()["id"]
    delete_response = client.delete(f'/api/todos/{todo_id}')
    assert delete_response.status_code == 200



''' Test case for deleting all todos '''

def test_delete_all_todos(client):
    ''' Add a test todo first '''
    client.post('/api/todos', json={
        "title": "Delete All Task",
        "description": "Delete all tasks test"
    })

    '''Delete all todos'''
    delete_all_response = client.delete('/api/todos')
    data = delete_all_response.get_json()
    assert delete_all_response.status_code == 200
    assert data["message"] == "All Todos deleted successfully!"

    ''' Verify that no todos exist '''
    response = client.get('/api/todos')
    data = response.get_json()
    assert response.status_code == 200
    assert len(data) == 0  # No todos should be left


''' Test case for updating a todo
'''
def test_update_todo(client):
    ''' Add a test todo first'''
    post_response = client.post('/api/todos', json={
        "title": "Old Title",
        "description": "Old Description"
    })
    todo_id = post_response.get_json()["id"]

    ''' Update the test todo '''
    update_response = client.put(f'/api/todos/{todo_id}', json={
        "title": "Updated Title",
        "description": "Updated Description"
    })
    data = update_response.get_json()
    assert update_response.status_code == 200
    assert data["message"] == "Todo updated successfully!"
    assert "todo" in data
    assert data["todo"]["title"] == "Updated Title"
    assert data["todo"]["description"] == "Updated Description"


