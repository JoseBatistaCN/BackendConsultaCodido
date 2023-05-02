import sys, os
sys.path.insert(0, os.path.abspath(".."))
from Models.cid10 import Cid10DAO
from Models.cid11 import Cid11DAO
from Models.sigtap import SigtapDAO
from Models.cif import CifDAO
from googletrans import Translator



class ConsultaController:
    def __init__(self):
        self.cid10_dao = Cid10DAO()
        self.cid11_dao = Cid11DAO()
        self.sigtap_dao = SigtapDAO()
        self.cif_dao = CifDAO()
        
    
    def consultaCid10(self, codigo):
        result = self.cid10_dao.get(codigo)
        return result
    
    def consultaCid11(self, codigo):
        result = self.cid11_dao.getCid11(codigo)
        for row in result:
            uri = row['uri']
            if uri != None:
                try:
                    resultApi = self.cid11_dao.getCid11ByAPI(uri)
                    resultApi['uri'] = uri
                    row.update(resultApi)
                except Exception as e:
                    print("Erro" + str(e))
                    continue
        return result
        
    def consultaCif(self, codigo):
        result = self.cif_dao.getCif(codigo)
        return result
    
        
    def consultaSigtap(self, codigo):
        result = self.sigtap_dao.get(codigo)
        return result