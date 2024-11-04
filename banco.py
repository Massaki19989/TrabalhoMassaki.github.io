from datetime import datetime
import sqlite3

class GerenciadorVendas():
    def __init__(self):
        self.data_atual = datetime.now()
    
    def obter_vendas_por_mes(self, maximo, pg):
        banco = sqlite3.connect('database/vendas.db')
        cursor = banco.cursor()
        cursor.execute("""
            SELECT id, nome, SUM(quantidade) as total_quantidade, dia, mes, ano, hora 
            FROM vendas 
            WHERE ano = ?
            GROUP BY nome, mes 
            ORDER BY total_quantidade DESC 
            LIMIT ? OFFSET ?
        """, (2023,maximo, pg))
        vendas = cursor.fetchall()

        banco.close()

        return vendas
    
    def cadastrar_vendas(self, nome, quantidade, dia, mes, ano):
        banco = sqlite3.connect('database/vendas.db')
        cursor = banco.cursor()
        
        hora = self.data_atual.hour

        nome_formatado = nome.capitalize()

        cursor.execute('INSERT INTO vendas (nome, quantidade, dia, mes, ano, hora) VALUES (?, ?, ?, ?, ?, ?)', 
                       (nome_formatado, quantidade, dia, mes, ano, hora))
        banco.commit()
        banco.close()

    def itens_para_deletar(self, maximo, pg):
        banco = sqlite3.connect('database/vendas.db')
        cursor = banco.cursor()
        cursor.execute('SELECT * FROM vendas LIMIT ? OFFSET ?', (maximo, pg))
        vendas = cursor.fetchall()
        banco.close()
        return vendas

    def deletar_by_id(self, id):
        banco = sqlite3.connect('database/vendas.db')
        cursor = banco.cursor()
        cursor.execute('DELETE FROM vendas WHERE id = ?', (id,))
        banco.commit()
        banco.close()

    def obter_vendas_do_mes(self, mes, maximo, pg, ano):
        banco = sqlite3.connect('database/vendas.db')
        cursor = banco.cursor()
        cursor.execute("""
            SELECT id, nome, SUM(quantidade) as total_quantidade, dia, mes, ano, hora FROM vendas WHERE mes = ? and ano = ? GROUP BY nome, mes ORDER BY total_quantidade DESC LIMIT ? OFFSET ?
        """, (mes, ano, maximo, pg))
        vendas = cursor.fetchall()

        banco.close()

        return vendas
    
    def obter_paginas_mes(self, mes, ):
        banco = sqlite3.connect('database/vendas.db')
        cursor = banco.cursor()
        cursor.execute(""" SELECT COUNT(DISTINCT nome) FROM vendas WHERE mes = ? """, (mes,))
        total = cursor.fetchone()[0]
        banco.close()
        return total
    
    def obter_paginas(self):
        banco = sqlite3.connect('database/vendas.db')
        cursor = banco.cursor()
        cursor.execute(""" SELECT COUNT(nome) FROM vendas""")
        total = cursor.fetchone()[0]
        banco.close()
        return total
    
    def obter_vendas_por_estacao(self, estacao, ano):
        banco = sqlite3.connect('database/vendas.db')
        cursor = banco.cursor()
        cursor.execute("""
            SELECT id, nome, SUM(quantidade) as total_quantidade, dia, mes, ano, hora 
            FROM vendas 
            WHERE ano = ?
            GROUP BY nome, mes 
            ORDER BY total_quantidade DESC 
        """, (ano,))
        vendas = cursor.fetchall()

        banco.close()

        vendasEstacao = []
        quantidade = []
        if estacao == 'primavera' or estacao == 'Primavera':
            for venda in vendas:
                if venda[4] >= 9 and venda[3] <= 31 and venda[4] <= 12:
                    if venda[4] == 12 and venda[3] >= 22:
                        pass
                    else:
                        if venda[4] == 9 and venda[3] <= 22:
                            pass
                        else:
                            vendasEstacao.append(venda[1])
                            quantidade.append(venda[2])
        elif estacao == 'verao' or estacao == 'Verao':
            for venda in vendas:
                if venda[3] >= 1 and venda[4] >= 1 and venda[3] <= 31 and venda[4] <= 3:
                    if venda[4] == 3 and venda >= 23:
                        pass
                    else:
                        vendasEstacao.append(venda[1])
                        quantidade.append(venda[2])
                else:
                    if venda[3] >= 21 and venda[3] <= 31 and venda[4] == 12:
                        vendasEstacao.append(venda[1])
                        quantidade.append(venda[2])

        elif estacao == 'outono' or estacao == 'Outono':
            for venda in vendas:
                if venda[4] >= 3 and venda[3] <= 31 and venda[4] <= 6:
                    if venda[4] == 6 and venda[3] >= 22:
                        pass
                    else:
                        if venda[3] <= 20 and venda[4] == 3:
                            pass
                        else:
                            vendasEstacao.append(venda[1])
                            quantidade.append(venda[2])
        elif estacao == 'inverno' or estacao == 'Inverno':
            for venda in vendas:
                if venda[4] >= 6 and venda[3] <= 31 and venda[4] <= 9:
                    if venda[4] == 9 and venda[3] >= 23:
                        pass
                    else:
                        if venda[4] == 9 and venda[3] <= 20:
                            pass
                        else:
                            vendasEstacao.append(venda[1])
                            quantidade.append(venda[2])

        return vendasEstacao, quantidade