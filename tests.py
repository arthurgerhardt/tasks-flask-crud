import pytest
import requests

# CRUD
BASE_URL = 'http://127.0.0.1:5000'
tasks = []

@pytest.fixture(scope="function", autouse=True)
def setup():
    """ Limpa a lista de tarefas antes de cada teste para evitar interferências. """
    global tasks
    tasks.clear()

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
    assert isinstance(response_json, dict)  # Garante que o retorno é um dicionário
    assert "tasks" in response_json
    assert "total_tasks" in response_json 

def test_get_task():
    if not tasks:
        pytest.skip("Nenhuma tarefa foi criada para testar.")

    task_id = tasks[0]
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 200
    response_json = response.json()
    assert isinstance(response_json, dict)  # Garante que o retorno é um dicionário
    assert response_json['id'] == task_id