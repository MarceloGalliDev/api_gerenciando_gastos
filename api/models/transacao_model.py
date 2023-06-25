from api import db
import enum

# para criar choices
class TipoEnum(enum.Enum):
    entrada = 1
    saida = 2

class Transacao(db.Model):
    __tablename__ = "transacao"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    tipo = db.Column(db.Enum(TipoEnum), nullable=False)
    #aqui relacionamos o id da conta com o campo conta_id, vai armazenar o id atrelado ao id da tabela conta
    conta_id = db.Column(db.Integer, db.ForeignKey('conta.id'))
    #aqui vamos chamar todas as transações atreladas a conta
    #atrelamos um relationship a Conta, adicionando o indicamento de processo inverso
    #quando chamar-mos o db.backref de uma conta, ele vai listar todas transações de uma conta
    # lazy='dynamic' é para retorna todas transações em uma mesma requisição
    conta = db.relationship("Conta", backref=db.backref("transacoes", lazy="dynamic"))