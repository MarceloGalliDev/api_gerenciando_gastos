from flask import make_response, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, create_refresh_token
from api import api

class RefreshTokenList(Resource):
    @jwt_required(refresh=True)
    def post(self):
        #aqui vamos utilizar o get_jwt_identity para receber o id atrelado a esse refresh token
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        refresh_token = create_refresh_token(identity=current_user)
        return make_response(jsonify({
            'access_token': access_token,
            'refresh_token': refresh_token,
        }), 200)

api.add_resource(RefreshTokenList, '/token/refresh')