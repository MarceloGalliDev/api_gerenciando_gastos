#aqui é o que define os métodos para cadastro de dados diretamente com o banco de dados

from ..models import conta_model
from api import db

#vamos receber uma conta como paramêtro
def cadastrar_conta(conta):
    conta_bd = conta_model.Conta(nome=conta.nome, descricao=conta.descricao, saldo=conta.saldo)
    #estamos adicionando a secão ao banco de dados adicionando a conta
    db.session.add(conta_bd)
    #aqui persistimos os dados
    db.session.commit()
    #retornando a conta
    return conta_bd    

def listar_contas():
    contas = conta_model.Conta.query.all()
    return contas

def listar_conta_id(id):
    #buscamos o model, filtramos com id e retornamos o primeiro
    conta = conta_model.Conta.query.filter_by(id=id).first()
    return conta
    
def remover_conta(conta):
    db.session.delete(conta)
    db.session.commit()
    
    
    
    
    
    
    