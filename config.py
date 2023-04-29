import os
import random, string
import psycopg2

class Config(object):
    CSRF_ENABLE = True
    SECRET = ""
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = None
    con = psycopg2.connect(host='database-consultas.cvqj6vrowliw.us-east-1.rds.amazonaws.com', database='postgres', user='postgres', password='consultasCOMP0439**')
    JSON_AS_ASCII = False

class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = '0.0.0.0'
    PORT_HOST = 8080
    URL_MAIN = f"http://{IP_HOST}:{PORT_HOST}"

app_config = {
    'development': DevelopmentConfig(),
}

app_active = 'development'