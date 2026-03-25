
from pydantic import BaseModel, Field, EmailStr

class AlunoCreate(BaseModel):
    nome: str = Field(..., min_length=3)
    idade: int = Field(..., ge=0)
    email: EmailStr