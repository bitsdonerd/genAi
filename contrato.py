from datetime import datetime
from typing import Tuple
from datetime import datetime, time
from pydantic import BaseModel, EmailStr,  PositiveFloat, PositiveInt, field_validator
from enum import Enum

# Validation erros (Enum)
class produtoEnum(str,Enum):
    produto1 = 'Produto 1'
    produto2 = 'Produto 2'
    produto3 = 'Produto 3'


# Classe do Pydantic (BaseModel)
class Vendas(BaseModel):
    """
    Modelo de dados para a classe Vendas.

    Args: 
        email (EmailStr): email do vendedor 
        data (datetime): data da venda
        valor (PositiveFloat): valor da venda
        quantidade (PositiveInt): quantidade de produto
        produto (produtoEnum): nome do produto
    """
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: produtoEnum

    @field_validator('produto')
    def categoria_deve_estar_no_enum(cls, v):
        return v