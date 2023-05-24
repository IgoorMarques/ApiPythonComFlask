from api import api
from flask_restful import Resource
from ..schemas import login_schema
from flask import request, make_response, jsonify
from ..services import usuario_service
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import timedelta


class LoginList(Resource):
    def post(self):
        ls = login_schema.LoginSchema()
        validate = ls.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            email = request.json["email"]
            senha = request.json["senha"]
            usuario_db = usuario_service.listar_usuario_email(email)
            if usuario_db and usuario_db.descripto_senha(senha):
                acess_token = create_access_token(
                    identity=usuario_db.id,
                    expires_delta=timedelta(seconds=300)
                )
                refresh_token = create_refresh_token(identity=usuario_db.id)
                return make_response(jsonify(
                    {
                        'acces_token': acess_token,
                        'refresh_token': refresh_token,
                        'mensagem': 'Login realizado com sucesso'
                    }
                ))
            else:
                return make_response(jsonify(
                    {
                        'mensagem': 'Credenciais inválidas'
                    }
                ))


api.add_resource(LoginList, '/login')
