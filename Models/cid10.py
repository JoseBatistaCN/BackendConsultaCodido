from flask import jsonify
import psycopg2
from psycopg2.extras import RealDictCursor

class Cid10DAO:
    def __init__(self):
        self.conn = psycopg2.connect(host='database-consultas.cvqj6vrowliw.us-east-1.rds.amazonaws.com', database='postgres', user='postgres', password='consultasCOMP0439**')
    
    def get(self, codigo):
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        
        cur.execute(f"""SELECT co_cid, no_cid FROM consultas.cid10
                    WHERE ( unaccent(no_cid)    ILIKE CONCAT('%', unaccent('{codigo}'),'%' )
                    OR ( no_cid 				ILIKE '%{codigo}%' )
                    OR ( co_cid 				ILIKE '%{codigo}%'));
                    """)
        
        rows = cur.fetchall()
        doencas = []
        for row in rows:
            doenca = {'codigo': row[0], 'titulo': row[1]}
            doencas.append(doenca)
        
        result = doencas
        return rows
