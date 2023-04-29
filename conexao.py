import psycopg2

con = psycopg2.connect(host='database-consultas.cvqj6vrowliw.us-east-1.rds.amazonaws.com', database='postgres', user='postgres', password='consultasCOMP0439**')
cur = con.cursor()

entrada = "vesícula"
sql =   f"SELECT * FROM consultas.cid11\
        WHERE ( LOWER(unaccent(titulo)) LIKE LOWER(CONCAT('%', unaccent('{entrada}'),'%' )))\
        OR ( LOWER(titulo) 				LIKE LOWER(CONCAT('%', unaccent('{entrada}'),'%' )))\
        OR ( LOWER(unaccent(title)) 	LIKE LOWER(CONCAT('%', unaccent('{entrada}'),'%' )))\
        OR ( LOWER(title) 				LIKE LOWER(CONCAT('%', unaccent('{entrada}'),'%' )))\
        OR ( LOWER(codigo) 				LIKE LOWER(CONCAT('%', unaccent('{entrada}'),'%' )));"

sql2 =   f"""SELECT co_cid, no_cid FROM consultas.cid10
WHERE ( LOWER(unaccent(no_cid)) LIKE LOWER(CONCAT('%', unaccent('b05'),'%' )))
OR ( LOWER(no_cid) 				LIKE LOWER(CONCAT('%', unaccent('b05'),'%' )))
OR ( LOWER(co_cid) 				LIKE LOWER(CONCAT('%', unaccent('b05'),'%' )));
"""

cur.execute(sql2)
recset = cur.fetchall()

for rec in recset:
    print (rec)
con.close()