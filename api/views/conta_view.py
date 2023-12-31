#views mostra nossa api

from flask import request, make_response, jsonify
from flask_restful import Resource
from ..schemas import conta_schema
from ..entidades import conta
from ..services import conta_service, usuario_service
from api import api
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..decorators import autorizacao_user

class ContaList(Resource):
    @jwt_required()
    def get(self):
        #vamos pegar o usuario logado pelo access token
        usuario = get_jwt_identity()
        #aqui recebemos os dados la do service
        contas = conta_service.listar_contas(usuario=usuario)
        #vamos transforma o arquivo do tipo python para o tipo json
        cs = conta_schema.ContaSchema(many=True)
        return make_response(cs.jsonify(contas), 200)
    
    
    @jwt_required()
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
            usuario = get_jwt_identity()
            conta_nova = conta.Conta(nome=nome, descricao=descricao, saldo=saldo, usuario=usuario)
            #aqui vamos cadastrar no banco de dados(service)
            result = conta_service.cadastrar_conta(conta_nova)
            #aqui retornamos como json
            return make_response(cs.jsonify(result), 201)

class ContaDetail(Resource):
    @autorizacao_user.conta_user
    def get(self, id):
        conta = conta_service.listar_conta_id(id)
        cs = conta_schema.ContaSchema()
        return make_response(cs.jsonify(conta), 200)
    
    
    @autorizacao_user.conta_user
    def put(self, id,):
        #verificamos se existe a conta pelo id
        conta_bd = conta_service.listar_conta_id(id)
        #vamos validar as info que vem através do corpo da requisição
        cs = conta_schema.ContaSchema()
        #estamos validando vindo atraves da nossa requisição com base no nosso ContaSchema
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            #recupero os dados a serem editados
            nome = request.json['nome']
            descricao = request.json['descricao']
            saldo = request.json['saldo']
            #criamos um novo objeto do tipo Conta com esses dados
            usuario = get_jwt_identity()
            conta_nova = conta.Conta(nome=nome, descricao=descricao, saldo=saldo, usuario=usuario)
            #enviaremos os dados para que sejam editados os dados einseridos no banco de dados
            result = conta_service.editar_conta(conta_bd, conta_nova)
            return make_response(cs.jsonify(result), 201)


    @autorizacao_user.conta_user
    def delete(self, id):
        #aqui buscamos o id
        conta = conta_service.listar_conta_id(id)
        conta_service.remover_conta(conta)
        return make_response('', 204)
        
api.add_resource(ContaList, '/contas')
api.add_resource(ContaDetail, '/contas/<int:id>')