from flask import Flask, request, jsonify
from models.task import Task
app = Flask(__name__)

# CRUD
# Create, Read, Update, Delete
# Tabela: Tarefa

tasks = []
task_id_control = 1

# Criando uma tarefa
@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data['title'], description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks )
    return jsonify({"message": "Nova tarefa criada com sucesso.", "id": new_task.id}), 201

# Lendo todas as tarefas
def get_tasks():
    tasks_list = [task.to_dict() for task in tasks]

    output = {
        "tasks": tasks_list,
        "total_tasks": len(tasks_list)
    }
    return jsonify(output)

# Lendo uma tarefa
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = None
    for t in tasks:
        if t.id == id:
         return jsonify(t.to_dict())
    return jsonify({"message": "Não foi possível encontrar a atividade."}), 404

# Atualizando uma tarefa
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break
    print(task)
        
    if task is None:
        return jsonify({"message": "Não foi possível encontrar a atividade."}), 404
    
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    print(task)
    return jsonify({"message": "Tarefa atualizada com sucesso."})

# Deletando uma tarefa
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break
    
    if task is None:
        return jsonify({"message": "Não foi possível encontrar a atividade."}), 404
    
    tasks.remove(task)
    return jsonify({"message": "Tarefa removida com sucesso."})

if __name__ == '__main__':
    app.run(debug=True)
