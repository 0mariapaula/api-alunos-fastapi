from sqlalchemy import create_engine
engine = create_engine("sqlite:///alunos.db")

from sqlalchemy.orm import declarative_base,sessionmaker
Base = declarative_base()
from sqlalchemy import Column, Integer, String
class Aluno(Base):
    __tablename__ = "alunos"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

    def __repr__(self):
        return f"Aluno(id={self.id}, nome='{self.nome}', idade={self.idade})"

#|CRIA TABELA NO BANCO DE DADOS SE ELA AINDA NÃO EXISTIR
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)