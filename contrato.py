from datetime import datetime
from typing import Tuple

from pydantic import BaseModel, EmailStr, validate_call, PositiveFloat, PositiveInt
from enum import Enum

# Validation erros (Enum)
class produtoEnum(str,Enum):
    produto1 = 'Produto 1'
    produto2 = 'Produto 2'
    produto3 = 'Produto 3'


# Classe do Pydantic (BaseModel)
class Vendas(BaseModel):
    email: EmailStr
    data: datetime
    hora: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: produtoEnum

    @validate_call('produto')
    def categoria_Enum(cls,v):
        return v