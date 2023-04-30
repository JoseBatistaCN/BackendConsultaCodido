import sys, os
sys.path.insert(0, os.path.abspath(".."))
from Models.cid10 import Cid10DAO
from Models.cid11 import Cid11DAO
from Models.sigtap import SigtapDAO



class ConsultaController:
    def __init__(self):
        self.cid10_dao = Cid10DAO()
        self.cid11_dao = Cid11DAO()
        self.sigtap_dao = SigtapDAO()
    
    def consultaCid10(self, codigo):
        result = self.cid10_dao.get(codigo)
        
        return result
    
    def consultaCid11(self, codigo):
        result = self.cid11_dao.getCid11(codigo)
        return result
        
    def consultaSigtap(self, codigo):
        result = self.sigtap_dao.get(codigo)
        return result