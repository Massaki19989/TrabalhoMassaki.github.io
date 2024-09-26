from flask import Flask, render_template, request
from datetime import datetime
import sqlite3

def obter_vendas():
    banco = sqlite3.connect('database/vendas.db')
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM vendas")
    vendas = cursor.fetchall()

    banco.close()

    return vendas

def cadastrar_vendas(nome, quantidade):
    banco = sqlite3.connect('database/vendas.db')
    cursor = banco.cursor()

    cursor.execute('INSERT into vendas (nome, quantidade, dia, mes, ano, hora) VALUES (?,?,?,?,?,?)', 
               (nome, quantidade, 25, 9, 2024, 10))
    banco.commit()
    banco.close()

app = Flask(__name__)

@app.route('/')
def inicial():
    vendas = obter_vendas()
    return render_template('home.html', vendas=vendas)

@app.route('/vender')
def vender():
    return render_template('vender.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    quantidades = request.form.getlist('quantidade[]')
    nomes = request.form.getlist('nome[]')

    for quantidade, nome in zip(quantidades, nomes):
        cadastrar_vendas(nome,quantidade)
        
    return "<script> document.location = './' </script>"

if __name__ == '__main__':
    app.run()