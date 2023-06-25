from api import api
from flask_restful import Resource
from ..schemas import login_schema
from flask import request, make_response, jsonify

class LoginList(Resource):
    def post(self):
        ls = login_schema.LoginSchema()
        #vamos enviar o login de requisição para validar os dados
        validate = ls.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        #veio no corpo da requisição
        email = request.json['email']
        