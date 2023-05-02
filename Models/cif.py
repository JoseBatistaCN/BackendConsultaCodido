from flask import jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
import requests
import urllib3
urllib3.disable_warnings()


class CifDAO:
    
    def __init__(self):
        # Realiza a conexão com o banco de dados PostgreSQL
        self.conn = psycopg2.connect(host='database-consultas.cvqj6vrowliw.us-east-1.rds.amazonaws.com', database='postgres', user='postgres', password='consultasCOMP0439**')
    

    def getCif(self, codigo):
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(
            f"""
            SELECT * FROM consultas.cif
            WHERE ( unaccent(titulo) ILIKE '%{codigo}%' ) OR
            ( titulo ILIKE '%{codigo}%' ) OR
            ( unaccent(title) ILIKE '%{codigo}%' ) OR
            ( title ILIKE '%{codigo}%' ) OR
            ( codigo ILIKE '%{codigo}%' )    
            """
            )
        rows = cur.fetchall()

        # doencas = []
        
        # for row in rows:
        #     doenca = {'uri': row[0], 'codigo': row[1], 'titulo': row[2], 
        #     'title': row[3], 'descricao': row[4], 'description': row[5]}
        #     doencas.append(doenca)    
              
        return rows
            
   
    def getToken(self):
           token_endpoint = 'https://icdaccessmanagement.who.int/connect/token'
           client_id = '5c9a97af-4946-4fb4-9f46-0b229cffda95_981673fd-7474-4926-a0b6-79eb272ff94d'
           client_secret = 'BCf7O5CnH1NQ7muc08Ea4HC11aySz0qMXO9I4cbjc2M='
           
           scope = 'icdapi_access'
           grant_type = 'client_credentials'
           
           cert = '_.who.int.crt'
           
           # get the OAUTH2 token
           
           # set data to post
           payload = {'client_id': client_id, 
           	   	      'client_secret': client_secret, 
                      'scope': scope, 
                      'grant_type': grant_type}
                      
           # make request
           r = requests.post(token_endpoint, data=payload, verify=False).json()
           return r['access_token']


    def getcifByAPI(self, url):
               # HTTP header fields to set
               headers = {'Authorization':  'Bearer '+ self.getToken(), 
                          'Accept': 'application/json', 
                          'Accept-Language': 'en',
               	'API-Version': 'v2'}
               # make request           
               json_data = requests.get(url, headers=headers, verify=False).json()
               relevant_data = {'title': json_data['title']['@value'],
                     'synonyms': [s['label']['@value'] for s in json_data['synonym']],
                     'definition': json_data['definition']['@value']}
               return relevant_data
