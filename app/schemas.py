from pydantic import BaseModel

class AlunoCreate(BaseModel):
    nome: str
    idade: int