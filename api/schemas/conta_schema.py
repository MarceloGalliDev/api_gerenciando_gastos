#define as regras
#aqui o schema define se a requisição vai passar a diante.

from api import ma
from ..models import conta_model
from marshmallow import fields
from ..schemas import transacao_schema

#aqui vamos validar o model
class ContaSchema(ma.SQLAlchemyAutoSchema):
    #esse transacoes é o mesmo do model de relationship
    #aqui temos uma conta > Nested > transações
    transacoes = ma.Nested(transacao_schema.TransacaoSchema, many=True)
    class Meta:
        model = conta_model.Conta
        load_instace = True
    
    #é requerido
    nome = fields.String(required=True)
    descricao = fields.String(required=True)
    saldo = fields.Float(required=True)
    usuario_id = fields.Integer(required=True)