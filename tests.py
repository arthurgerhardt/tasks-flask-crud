import pytest
import requests

# CRUD
BASE_URL = 'http://127.0.0.1:5000'

tasks = []

def test_create_task():
    new_task_data = {
        "title": "Nova Tarefa",
        "description": "Descrição da nova tarefa."
    }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.status_code == 201
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json['id'])  # Store the task ID for cleanup
    
def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks") 
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json 
    assert "total_tasks" in response_json 