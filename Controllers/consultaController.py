import sys, os
sys.path.insert(0, os.path.abspath(".."))
from Models.cid10 import Cid10DAO

class ConsultaController:
    def __init__(self):
        # Cria uma instância da classe CID10DAO
        self.cid10_dao = Cid10DAO()
    
    def getByCodigo(self, codigo):
        # Chama o método getByCodigo da classe CID10DAO para realizar a consulta ao banco de dados
        result = self.cid10_dao.getByCodigo(codigo)
        
        # Retorna o resultado em um objeto JSON
        return result
    
    def getByTitulo(self, titulo):
        # Chama o método getByTitulo da classe CID10DAO para realizar a consulta ao banco de dados
        result = self.cid10_dao.getByTitulo(titulo)
        
        # Retorna o resultado em um objeto JSON
        return result
    
    
    