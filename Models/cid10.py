from flask import jsonify
import psycopg2


class Cid10DAO:
    def __init__(self):
        # Realiza a conexão com o banco de dados PostgreSQL
        self.conn = psycopg2.connect(host='database-consultas.cvqj6vrowliw.us-east-1.rds.amazonaws.com', database='postgres', user='postgres', password='consultasCOMP0439**')
    
    def get(self, codigo):
        # Cria um cursor para executar as consultas SQL
        cur = self.conn.cursor()
        
        # Executa a consulta SQL
        cur.execute(f"""SELECT co_cid, no_cid FROM consultas.cid10
                    WHERE ( LOWER(unaccent(no_cid)) LIKE LOWER(CONCAT('%', unaccent('{codigo}'),'%' )))
                    OR ( LOWER(no_cid) 				LIKE LOWER(CONCAT('%', unaccent('{codigo}'),'%' )))
                    OR ( LOWER(co_cid) 				LIKE LOWER(CONCAT('%', unaccent('{codigo}'),'%' )));
                    """)
        
        # Obtém os resultados da consulta
        rows = cur.fetchall()
        doencas = []
        for row in rows:
            doenca = {'codigo': row[0], 'titulo': row[1]}
            doencas.append(doenca)
        
        result = doencas
        # Converte os resultados para um objeto JSON usando a função jsonify do Flask
        return result
