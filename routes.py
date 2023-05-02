from flask import Blueprint, jsonify, request
from Controllers.consultaController import ConsultaController


routesCodigo = Blueprint('routesCodigo', __name__)

@routesCodigo.route('/')
def index():
    return jsonify({"Codigo": 'B05', "Doenca": "Sarampo"})

@routesCodigo.route('/cid10/<string:codigo>', methods=['GET'])
def getByCodigo(codigo):
    result = ConsultaController().consultaCid10(codigo)
    return jsonify(result)


@routesCodigo.route('/cid11/<string:codigo>', methods=['GET'])
def getCid11(codigo):
     result = ConsultaController().consultaCid11(codigo)
     return jsonify(result)
      
@routesCodigo.route('/sigtap/<string:codigo>', methods=['GET'])
def getSigtap(codigo):
     result = ConsultaController().consultaSigtap(codigo)
     return jsonify(result)

@routesCodigo.route('/cif/<string:codigo>', methods=['GET'])
def getCif(codigo):
     result = ConsultaController().consultaCif(codigo)
     return jsonify(result)
     
