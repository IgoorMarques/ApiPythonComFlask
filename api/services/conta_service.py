from api import db
from ..models import conta_model


def listar_contas(usuario):
    contas = conta_model.Conta.query.filter_by(usuario_id=usuario).all()
    return contas


def listar_conta_id(id):
    conta = conta_model.Conta.query.filter_by(id=id).first()
    return conta


def cadastrar_conta(conta):
    conta_db = conta_model.Conta(nome=conta.nome, resumo=conta.resumo, valor=conta.valor, usuario_id=conta.usuario)
    db.session.add(conta_db)
    db.session.commit()
    return conta_db


def atualizar_conta(conta, conta_nova):
    conta.nome = conta_nova.nome
    conta.resumo = conta_nova.resumo
    conta.valor = conta_nova.valor
    db.session.commit()
    return conta


def excluir_conta(conta):
    db.session.delete(conta)
    db.session.commit()


def altera_saldo_conta(conta_id, operacao, tipo_funcao, valor_antigo=None):
    # tipo_funcao == 1 -> cadastro de operação
    # tipo_funcao == 2 -> atualização de operação
    # tipo_funcao == 3 -> remoção de operação
    conta = listar_conta_id(conta_id)
    if tipo_funcao == 1:
        if operacao.tipo == 'entrada':
            conta.valor += operacao.custo
        else:
            conta.valor -= operacao.custo

    elif tipo_funcao == 2:
        if operacao.tipo == 'entrada':
            conta.valor -= valor_antigo
            conta.valor += operacao.custo
        else:
            conta.valor += valor_antigo
            conta.valor -= operacao.custo
    else:
        if operacao.tipo.value == 'entrada':
            conta.valor -= operacao.custo
        else:
            conta.valor += operacao.custo

    db.session.commit()
