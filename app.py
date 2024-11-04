from flask import Flask, render_template, request, redirect
from banco import GerenciadorVendas
from datetime import datetime

venda_db = GerenciadorVendas()

app = Flask(__name__)

@app.route('/')
def inicial():
    maximo = 15
    try:
        pg = (int(request.args.get('pg', 1))-1)*maximo
    except:
        pg = 0
    vendas = venda_db.obter_vendas_por_mes(maximo, pg)
    return render_template('home.html', vendas=vendas)

@app.route('/<int:mes>')
def mes(mes):
    data_atual = datetime.now()
    try:
        ano = int(request.args.get('ano'))
    except:
        ano = data_atual.year

    anoAtual = data_atual.year
    novoAno = anoAtual
    anos = [ano]
    quantidadeDeAnos = 0
    while quantidadeDeAnos < 14:
        if novoAno != ano:
            anos.append(novoAno)
        novoAno = novoAno - 1
        quantidadeDeAnos = quantidadeDeAnos + 1

    nomeMes = 'Este mês não existe'

    if mes == 1:
        nomeMes = 'Janeiro'
    elif mes == 2:
        nomeMes = 'Fevereiro'
    elif mes == 3:
        nomeMes = 'Março'
    elif mes == 4:
        nomeMes = 'Abril'
    elif mes == 5:
        nomeMes = 'Maio'
    elif mes == 6:
        nomeMes = 'Junho'
    elif mes == 7:
        nomeMes = 'Julho'
    elif mes == 8:
        nomeMes = 'Agosto'
    elif mes == 9:
        nomeMes = 'Setembro'
    elif mes == 10:
        nomeMes = 'Outubro'
    elif mes == 11:
        nomeMes = 'Novembro'
    elif mes == 12:
        nomeMes = 'Dezembro'

    maximo = 10
    try:
        pg = (int(request.args.get('pg', 1)) - 1) * maximo
        pgAtual = int(request.args.get('pg', 1))
    except:
        pg = 0
        pgAtual = 1


    numeroPaginas = (venda_db.obter_paginas_mes(mes) + maximo - 1) // maximo

    proximaPg = pgAtual + 1

    if proximaPg > numeroPaginas:
        proximaPg = numeroPaginas

    if pgAtual > 0:
        pgAnterior = pgAtual - 1
    else:
        pgAnterior = 0

    
    vendaMes = venda_db.obter_vendas_do_mes(mes, maximo, pg, ano)
    return render_template('meses.html', vendas = vendaMes, nomeMes = nomeMes, numeroPaginas = numeroPaginas, pgAtual = pgAtual, pgAnterior = pgAnterior, proximaPg = proximaPg, ultimaPg = numeroPaginas, anos = anos)


@app.route('/vender')
def vender():
    data_atual = datetime.now()
    dia = data_atual.day
    mes = data_atual.month
    ano = data_atual.year
    return render_template('vender.html', dia = dia, mes = mes, ano = ano)

@app.route('/enviar', methods=['POST'])
def enviar():
    data_atual = datetime.now()
    quantidades = request.form.getlist('quantidade[]')
    nomes = request.form.getlist('nome[]')
    try:
        dia = request.form.get('dia')
        mes = request.form.get('mes')
        ano = request.form.get('ano')
    except:
        dia = data_atual.day
        mes = data_atual.month
        ano = data_atual.year

    for quantidade, nome in zip(quantidades, nomes):
        if nome != '' and quantidade != '':
            venda_db.cadastrar_vendas(nome,quantidade, dia, mes, ano)
        
    return redirect('./')

@app.route('/deletar')
def pagina_deletar():
    maximo = 30
    try:
        pg = (int(request.args.get('pg', 1)) - 1) * maximo
        pgAtual = int(request.args.get('pg', 1))
    except:
        pg = 0
        pgAtual = 1


    numeroPaginas = (venda_db.obter_paginas() + maximo - 1) // maximo

    proximaPg = pgAtual + 1

    if proximaPg > numeroPaginas:
        proximaPg = numeroPaginas

    if pgAtual > 0:
        pgAnterior = pgAtual - 1
    else:
        pgAnterior = 0

    itens = venda_db.itens_para_deletar(maximo, pg)

    return render_template('deletar.html', itens=itens, numeroPaginas = numeroPaginas, pgAtual = pgAtual, pgAnterior = pgAnterior, proximaPg = proximaPg, ultimaPg = numeroPaginas)

@app.route('/deletar/<int:id>')
def deletar(id):
    venda_db.deletar_by_id(id)
    return redirect('/deletar')

@app.route('/estacao')
def estacao():
    maximo = 2
    try:
        pg = (int(request.args.get('pg', 1))-1)*maximo
    except:
        pg = 0
    vendas = venda_db.obter_vendas_por_mes(maximo, pg)
    return render_template('estacao.html', vendas=vendas)

@app.route('/estacao/<string:estacao>')
def est(estacao):

    data_atual = datetime.now()
    try:
        ano = int(request.args.get('ano'))
    except:
        ano = data_atual.year

    anoAtual = data_atual.year
    novoAno = anoAtual
    anos = [ano]
    quantidadeDeAnos = 0
    while quantidadeDeAnos < 14:
        if novoAno != ano:
            anos.append(novoAno)
        novoAno = novoAno - 1
        quantidadeDeAnos = quantidadeDeAnos + 1

    maximo = 15
    try:
        pg = (int(request.args.get('pg', 1))-1)*maximo
        pgAtual = int(request.args.get('pg'))
    except:
        pg = 0
        pgAtual = 1
    vendas, quantidade = venda_db.obter_vendas_por_estacao(estacao, ano)

    quantidadeItens = len(vendas)

    numeroPaginas = (quantidadeItens+maximo-1)//maximo
    proximaPagina = pgAtual + 1
    pgAnterior = pgAtual - 1
    if proximaPagina > numeroPaginas:
        proximaPagina = numeroPaginas

    if pgAnterior < 1:
        pgAnterior = 1

    vendasPaginadas = vendas[pg:pg + maximo]
    quantidadePaginada = quantidade[pg:pg + maximo]

    print(quantidadeItens)
    return render_template('estacoes.html', vendas=vendasPaginadas, quantidade=quantidadePaginada, numeroPaginas=numeroPaginas, pgAnterior=pgAnterior, proximaPg=proximaPagina, pgAtual=pgAtual, estacao=estacao, zip=zip, anos=anos)
    
    



if __name__ == '__main__':
    app.run()


"""
Filtrar por Ano
"""