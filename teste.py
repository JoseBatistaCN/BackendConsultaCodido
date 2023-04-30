from flask import jsonify
import psycopg2
import psycopg2.extras
import json

def getCid11(codigo):
    conn = psycopg2.connect(host='database-consultas.cvqj6vrowliw.us-east-1.rds.amazonaws.com', database='postgres', user='postgres', password='consultasCOMP0439**')
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(
        f"""
        SELECT * FROM consultas.cid11
        WHERE ( unaccent(titulo) LIKE '{codigo}' ) OR
        ( titulo LIKE '{codigo}' ) OR
        ( unaccent(title) LIKE '{codigo}' ) OR
        ( title LIKE '{codigo}' ) OR
        ( codigo LIKE '{codigo}' )
        """
        )
    
    rows = cur.fetchall()
    
    print(json.dumps(rows, ensure_ascii=False))

    
    
getCid11("Cólera")
