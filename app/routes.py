from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    nome = "Delcio"
    dados = {"profissao": "Dev Jr", "idade": 37}
    return render_template('index.html', nome=nome, dados=dados)


@app.route('/contato')
def contato():
    contato = {
        "contato": 1,
        "nome": "Contato 1",
        "telefone": "84999999999",
        "descricao": "Este é o primeiro contato"
    }
    return render_template('contato.html', contato=contato)
