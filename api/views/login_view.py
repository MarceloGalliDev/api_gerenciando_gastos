from api import api
from flask_restful import Resource
from ..schemas import login_schema
from flask import request, make_response, jsonify
from ..services.usuario_service import listar_usuarios_email
from flask_jwt_extended import create_access_token
from datetime import timedelta

class LoginList(Resource):
    def post(self):
        ls = login_schema.LoginSchema()
        #vamos enviar o login de requisição para validar os dados
        validate = ls.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        #veio no corpo da requisição
        email = request.json['email']
        senha = request.json['senha']
        #aqui usamos a função listar usuario email para buscar pelo email em nosso banco de dados
        usuario_bd = listar_usuarios_email(email)
        #aqui fazemos uma  verificação do email e senha recebidos
        if usuario_bd and usuario_bd.ver_senha(senha):
            #vamos criar token
            access_token = create_access_token(
                # aqui estamos atrelando o token ao usuario
                identity=usuario_bd.id,
                #tempo de validade do token
                expires_delta=timedelta(seconds=200)
            )
            return make_response(jsonify({
                'access_token': access_token,
                'message': 'Login realizado com sucesso!'
            }), 200)
        return make_response(jsonify({
            'message': 'Credenciais inválidas!'
        }), 401)

api.add_resource(LoginList, '/login')