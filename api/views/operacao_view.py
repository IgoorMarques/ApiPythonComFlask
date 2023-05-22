from flask_restful import Resource
from ..schemas import operacao_schema
from flask import request, make_response, jsonify
from ..entidades import operacao
from ..services import operacao_service, conta_service
from api import api


class OperacaoList(Resource):
    def get(self):
        operacoes = operacao_service.listar_operacoes()
        os = operacao_schema.OperacaoSchema(many=True)
        return make_response(os.jsonify(operacoes), 201)

    def post(self):
        os = operacao_schema.OperacaoSchema()
        validate = os.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            resumo = request.json["resumo"]
            custo = request.json["custo"]
            tipo = request.json["tipo"]
            conta = request.json["conta_id"]
            if conta_service.listar_conta_id(conta) is None:
                return make_response("Conta não existe", 404)
            else:
                operacao_nova = operacao.Operacao(
                    nome=nome,
                    resumo=resumo,
                    custo=custo,
                    tipo=tipo,
                    conta=conta
                )
            resultado = operacao_service.cadastrar_operacao(operacao_nova)
            return make_response(os.jsonify(resultado), 201)


class OperacaoDetail(Resource):
    def get(self, id):
        operacao = operacao_service.listar_operacao_id(id)
        if operacao is None:
            return make_response(jsonify("Operacao não encontrada"), 404)
        os = operacao_schema.OperacaoSchema()
        return make_response(os.jsonify(operacao), 200)

    def put(self, id):
        operacao_db = operacao_service.listar_operacao_id(id)
        if operacao_db is None:
            return make_response(jsonify("Operação não encontrada"), 404)
        os = operacao_schema.OperacaoSchema()
        validate = os.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            resumo = request.json["resumo"]
            custo = request.json["custo"]
            tipo = request.json["tipo"]
            conta = request.json["conta_id"]
            if conta_service.listar_conta_id(conta) is None:
                return make_response("Conta não existe", 404)
            else:
                operacao_nova = operacao.Operacao(
                    nome=nome,
                    resumo=resumo,
                    custo=custo,
                    tipo=tipo,
                    conta=conta
                )
            resultado = operacao_service.atualizar_operacao(
                operacao=operacao_db,
                operacao_nova=operacao_nova
            )
            return make_response(os.jsonify(resultado), 201)

    def delete(self, id):
        operacao = operacao_service.listar_operacao_id(id)
        if operacao is None:
            return make_response(jsonify("Conta não encontrada"), 404)
        operacao_service.excluir_operacao(operacao)
        return make_response(jsonify("Removido com sucesso!"), 204)


api.add_resource(OperacaoList, '/operacoes')
api.add_resource(OperacaoDetail, '/operacoes/<int:id>')
