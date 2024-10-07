from datetime import datetime
import sqlite3

class GerenciadorVendas():
    def __init__(self):
        self.data_atual = datetime.now()
    
    def obter_vendas_por_mes(self):
        banco = sqlite3.connect('database/vendas.db')
        cursor = banco.cursor()
        cursor.execute("""
            SELECT id, nome, SUM(quantidade) as total_quantidade, dia, mes, ano, hora FROM vendas GROUP BY nome, mes ORDER BY total_quantidade DESC
        """)
        vendas = cursor.fetchall()

        banco.close()

        return vendas
    
    def cadastrar_vendas(self, nome, quantidade):
        banco = sqlite3.connect('database/vendas.db')
        cursor = banco.cursor()

        dia = self.data_atual.day
        mes = self.data_atual.month
        ano = self.data_atual.year
        hora = self.data_atual.hour

        nome_formatado = nome.capitalize()

        cursor.execute('INSERT INTO vendas (nome, quantidade, dia, mes, ano, hora) VALUES (?, ?, ?, ?, ?, ?)', 
                       (nome_formatado, quantidade, dia, mes, ano, hora))
        banco.commit()
        banco.close()

    def itens_para_deletar(self):
        banco = sqlite3.connect('database/vendas.db')
        cursor = banco.cursor()
        cursor.execute('SELECT * FROM vendas')
        vendas = cursor.fetchall()
        banco.close()
        return vendas
    
    def deletar_by_id(self, id):
        banco = sqlite3.connect('database/vendas.db')
        cursor = banco.cursor()
        cursor.execute('DELETE FROM vendas WHERE id = ?', (id,))
        banco.commit()
        banco.close()

    def obter_vendas_do_mes(self, mes):
        banco = sqlite3.connect('database/vendas.db')
        cursor = banco.cursor()
        cursor.execute("""
            SELECT id, nome, SUM(quantidade) as total_quantidade, dia, mes, ano, hora FROM vendas WHERE mes = ? GROUP BY nome, mes ORDER BY total_quantidade DESC
        """, (mes,))
        vendas = cursor.fetchall()

        banco.close()

        return vendas