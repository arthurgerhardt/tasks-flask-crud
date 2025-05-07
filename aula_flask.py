from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask funcionando com sucesso. Vamos para a programação."

if __name__ == '__main__':
    app.run(debug=True)
