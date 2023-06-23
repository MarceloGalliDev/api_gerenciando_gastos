from flask import request, make_response, jsonify
from flask_restful import Resource
from ..schemas import conta_schema
from ..entidades import conta
from ..services import conta_service

class ContaList(Resource):
    def post(self):
        #criando instancia 
        cs = conta_schema.ContaSchema()
        #validando dados(schema)
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            descricao = request.json['descricao']
            saldo = request.json['saldo']
            #aqui estamos criando um objeto do tipo conta e inserindo os dados nele(entidade)
            conta_nova = conta.Conta(nome=nome, descricao=descricao, saldo=saldo)
            #aqui vamos cadastrar no banco de dados(service)
            result = conta_service.cadastrar_conta(conta_nova)
            return make_response(jsonify(result), 201)

class ContaDetail(Resource):
    pass