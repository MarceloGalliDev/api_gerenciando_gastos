#aqui é o que define os métodos para cadastro de dados diretamente com o banco de dados

from ..models import conta_model
from api import db

#vamos receber uma conta como paramêtro
def cadastrar_conta(conta):
    conta_bd = conta_model.Conta(nome=conta.nome, descricao=conta.descricao, saldo=conta.saldo)
    #estamos adicionando a secão ao banco de dados adicionando a conta
    db.session.add(conta_bd)
    
    
    
    
    
    
    
    
    
    
    
    
    