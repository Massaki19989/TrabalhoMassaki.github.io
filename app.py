from flask import Flask, render_template, request, redirect
from banco import GerenciadorVendas

venda_db = GerenciadorVendas()

app = Flask(__name__)

@app.route('/')
def inicial():
    vendas = venda_db.obter_vendas_por_mes()
    return render_template('home.html', vendas=vendas)

@app.route('/vender')
def vender():
    return render_template('vender.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    quantidades = request.form.getlist('quantidade[]')
    nomes = request.form.getlist('nome[]')

    for quantidade, nome in zip(quantidades, nomes):
        if nome != '' and quantidade != '':
            venda_db.cadastrar_vendas(nome,quantidade)
        
    return redirect('./')

@app.route('/deletar')
def pagina_deletar():
    itens = venda_db.itens_para_deletar()

    return render_template('deletar.html', itens=itens)

@app.route('/deletar/<int:id>')
def deletar(id):
    venda_db.deletar_by_id(id)
    return redirect('/deletar')

@app.route('/estacao')
def estacao():
    vendas = venda_db.obter_vendas_por_mes()
    return render_template('estacao.html', vendas=vendas)

if __name__ == '__main__':
    app.run()