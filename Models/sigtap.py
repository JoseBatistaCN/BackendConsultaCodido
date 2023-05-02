import psycopg2
import psycopg2.extras
import json

class SigtapDAO:
    def __init__(self):
        # Realiza a conexão com o banco de dados PostgreSQL
        self.conn = psycopg2.connect(host='database-consultas.cvqj6vrowliw.us-east-1.rds.amazonaws.com', database='postgres', user='postgres', password='consultasCOMP0439**')
    
    def get(self, codigo):
        # Cria um cursor para executar as consultas SQL
        cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.connection.set_client_encoding('UTF8')
        
        # Executa a consulta SQL
        cur.execute(f"""
                   SET search_path TO consultas;

                    SELECT 	p.co_procedimento 	AS codigo,
            		p.no_procedimento 	AS titulo,
            		dsc.ds_procedimento AS descricao,
            		d.no_detalhe 		AS detalhe,
            		cid.no_cid  		AS doencas,
            		f.no_financiamento 	AS financiamento,
            		r.no_rubrica 		AS rubrica,
            		ROUND(p.VL_IDADE_MINIMA::numeric/12.0, 1) AS idade_min,
            		ROUND(p.VL_IDADE_MAXIMA::numeric/12.0, 1) AS idade_max,
            		p.VL_SH 			AS valor_servico_hospitalar,
            		p.VL_SA 			AS valor_servico_ambulatorial,
            		p.VL_SP 			AS valor_servico_profissional,
            		p.dt_competencia 	AS data
                	FROM 		tb_procedimento 		p
                	LEFT JOIN tb_financiamento			f	ON (p.co_financiamento  = f.no_financiamento)
                	LEFT JOIN tb_rubrica 				r 	ON (p.co_rubrica 		= r.co_rubrica)
                	LEFT JOIN rl_procedimento_cid 		pc	ON (p.co_procedimento 	= pc.co_procedimento)
                	LEFT JOIN tb_descricao 				dsc ON (p.co_procedimento 	= dsc.co_procedimento)
                	LEFT JOIN rl_procedimento_detalhe 	pd 	ON (p.co_procedimento 	= pd.co_procedimento)
                	LEFT JOIN tb_detalhe 				d 	ON (pd.co_detalhe 		= d.co_detalhe)
                	LEFT JOIN cid10						cid	ON (cid.co_cid			= pc.co_cid)
                    WHERE p.no_procedimento ILIKE '%{codigo}%'
                    OR p.co_procedimento ILIKE '%{codigo}%'
                    LIMIT 5;
                    """)
        
        # Obtém os resultados da consulta
        rows = cur.fetchall()
        doencas = []
        
        for row in rows:
            doenca = {'codigo': row[0], 'titulo': row[1], 'descricao': row[2], 'detalhe': row[3], 'doencas': row[4], 'financiomento': row[5], 'rubrica': row[6]}
            doencas.append(doenca)
        
        
        return doencas