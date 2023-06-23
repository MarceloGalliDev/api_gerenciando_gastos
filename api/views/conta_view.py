#views mostra nossa api

from flask import request, make_response, jsonify
from flask_restful import Resource
from ..schemas import conta_schema
from ..entidades import conta
from ..services import conta_service
from api import api

class ContaList(Resource):
    def get(self):
        #aqui recebemos os dados la do service
        contas = conta_service.listar_contas()
        #vamos transforma o arquivo do tipo python para o tipo json
        cs = conta_schema.ContaSchema(many=True)
        return make_response(cs.jsonify(contas), 200)
    
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
            #aqui retornamos como json
            return make_response(cs.jsonify(result), 201)

class ContaDetail(Resource):
    def get(self, id):
        conta = conta_service.listar_conta_id(id)
        if conta is None:
            return make_response(jsonify("Conta não encontrada!"), 404)
        cs = conta_schema.ContaSchema()
        return make_response(cs.jsonify(conta), 200)

    def delete(self, id):
        #aqui buscamos o id
        conta = conta_service.listar_conta_id(id)
        if conta is None:
            return make_response(jsonify("Conta não encontrada!"), 404)
        conta_service.remover_conta(conta)
        return make_response('', 204)
        
api.add_resource(ContaList, '/contas')
api.add_resource(ContaDetail, '/contas/<int:id>')