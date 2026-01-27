from flask import Flask, request, render_template
from models.tarefa import Tarefa

app = Flask(__name__)

# Rotas (endpoints)

@app.route('/') # Rota quando for acessado "/"
def home():
    return render_template('home.html', titulo='Home')


@app.route('/agenda', methods=['GET', 'POST'])
def agenda():
    tarefa = None
    if request.method == 'POST':
        titulo_tarefa = request.form['titulo-tarefa']
        data_conclusao = request.form['data-conclusao']
        tarefa = Tarefa(titulo_tarefa, data_conclusao)

    return render_template('agenda.html', titulo='Agenda', tarefa=tarefa)

@app.route('/ola') # Rota quando for acessado "/ola"
def ola_mundo():
    return render_template('ola.html', titulo='Olá!', nome='Flask')