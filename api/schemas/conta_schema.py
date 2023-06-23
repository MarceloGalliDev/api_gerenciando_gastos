#define as regras
#aqui o schema define se a requisição vai passar a diante.

from api import ma
from ..models import conta_model
from marshmallow import fields

#aqui vamos validar o model
class ContaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = conta_model.Conta
        load_instace = True
    
    #é requerido
    nome = fields.String(required=True)
    descricao = fields.String(required=True)
    saldo = fields.Float(required=True)