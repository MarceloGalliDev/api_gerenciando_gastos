from flask_restful import Resource
from api import api
from ..schemas import transacao_schema
from flask import request, make_response, jsonify
from ..entidades import transacao
from ..services import transacao_service, conta_service

class TransacaoList(Resource):
    def get(self):
        transacoes = transacao_service.listar_transacoes()
        cs = transacao_schema.TransacaoSchema(many=True)
        return make_response(cs.jsonify(transacoes), 200)


    def post(self):
        cs = transacao_schema.TransacaoSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            valor = request.json["valor"]
            tipo = request.json["tipo"]
            conta = request.json["conta_id"]
            if conta_service.listar_conta_id(conta) is None:
                return make_response("Conta não existe", 404)
            else:
                #os valors aqui citados, são os recebidos acima
                transacao_nova = transacao.Transacao(nome=nome, descricao=descricao,
                                                     valor=valor, tipo=tipo, conta=conta)
                result = transacao_service.cadastrar_transacao(transacao_nova)
                return make_response(cs.jsonify(result), 201)

class TransacaoDetail(Resource):
    def get(self, id):
        transacao = transacao_service.listar_transacao_id(id)
        if transacao is None:
            return make_response(jsonify("Transação não encontrada!"), 404)
        cs = transacao_schema.TransacaoSchema()
        return make_response(cs.jsonify(transacao), 200)


    def put(self, id):
        transacao_bd = transacao_service.listar_transacao_id(id)
        if transacao_bd is None:
            return make_response(jsonify("Transação não encontrada!"), 404)
        cs = transacao_schema.TransacaoSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            valor = request.json["valor"]
            tipo = request.json["tipo"]
            conta = request.json["conta_id"]
            if conta_service.listar_conta_id(conta) is None:
                return make_response('Conta não encontrada!', 400)
            else:
                transacao_nova = transacao.Transacao(nome=nome, descricao=descricao,
                                                    valor=valor, tipo=tipo, conta=conta)
                result = transacao_service.editar_transacao(transacao_bd, transacao_nova)
                return make_response(cs.jsonify(result), 200)


    def delete(self, id):
        transacao = transacao_service.listar_transacao_id(id)
        if transacao is None:
            return make_response(jsonify("Transação não encontrada!"), 404)
        transacao_service.remover_transacao(transacao)
        return make_response('', 204)

api.add_resource(TransacaoList, '/transacoes')
api.add_resource(TransacaoDetail, '/transacoes/<int:id>')