from flask import Flask
from models.task import Task

app = Flask(__name__)

# CRUD
# Create, Read, Update, Delete
# Tabela: Tarefa

tasks = []

if __name__ == '__main__':
    app.run(debug=True)
