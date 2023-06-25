from flask_restful import Resource
from api import api
from ..schemas import usuario_schema
from flask import request, make_response, jsonify
from ..entidades import usuario
from ..services import usuario_service

class UsuarioList(Resource):
    def post(self):
        # estamos instanciando um schema
        us = usuario_schema.UsuarioSchema()
        # validaremos a requisição
        validate = us.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            # aqui capturamos os atributos da requisição
            nome = request.json["nome"]
            email = request.json["email"]
            senha = request.json["senha"]
            # aqui criamos uma instância utilizando o entidades
            usuario_novo = usuario.Usuario(nome=nome, email=email, senha=senha)
            result = usuario_service.cadastrar_usuario(usuario_novo)
            return make_response(us.jsonify(result), 201)
        
api.add_resource(UsuarioList, '/usuarios')