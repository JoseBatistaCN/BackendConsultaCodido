from flask import Blueprint, jsonify, request
from Controllers.consultaController import ConsultaController


routesCodigo = Blueprint('routesCodigo', __name__)

@routesCodigo.route('/')
def index():
    return jsonify({"Codigo": 'B05', "Doenca": "Sarampo"})

@routesCodigo.route('/codigoCid10/<string:codigo>', methods=['GET'])
def getByCodigo(codigo):
    result = ConsultaController().getByCodigo(codigo)
    return jsonify(result)

@routesCodigo.route('/titulo/<string:titulo>', methods=['GET'])
def getByTitulo(titulo):
    result = ConsultaController.getByTitulo(titulo)
    return jsonify(result)