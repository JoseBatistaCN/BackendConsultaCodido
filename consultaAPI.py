import requests
import urllib3
urllib3.disable_warnings()

def getToken():
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

# access ICD API

def get(token):
           uri = '"https://id.who.int/icd/entity?q=cholera"'
           # HTTP header fields to set
           headers = {'Authorization':  'Bearer '+token, 
                      'Accept': 'application/json', 
                      'Accept-Language': 'en',
           	'API-Version': 'v2'}
           # make request           
           json_data = requests.get(uri, headers=headers, verify=False)
           relevant_data = {'title': json_data['title']['@value'],
                 'synonyms': [s['label']['@value'] for s in json_data['synonym']],
                 'definition': json_data['definition']['@value']}
           print(json_data)
           
token = getToken()
get(token)
