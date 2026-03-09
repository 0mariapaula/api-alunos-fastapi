
from sqlalchemy import Column, Integer, String
from app.database import Base  # Corrigido o caminho do import

class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

    def __repr__(self):
        return f"Aluno(id={self.id}, nome='{self.nome}', idade={self.idade})"