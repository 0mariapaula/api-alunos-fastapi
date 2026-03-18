from fastapi import APIRouter, HTTPException
from app.database import SessionLocal
from app.models import Aluno
from app.schemas import AlunoCreate

router = APIRouter()
@router.post("/alunos")
def criar_aluno(aluno: AlunoCreate):
	db = SessionLocal()
	try:
		novo_aluno = Aluno(
			nome=aluno.nome,
			idade=aluno.idade
		)
		db.add(novo_aluno)
		db.commit()
		db.refresh(novo_aluno)
		return {
			"id": novo_aluno.id,
			"nome": novo_aluno.nome,
			"idade": novo_aluno.idade
		}
	finally:
		db.close()

@router.get("/alunos")
def listar_alunos():
	db = SessionLocal()
	try:
		alunos = db.query(Aluno).all()
		return alunos
	finally:
		db.close()

@router.get("/alunos/{id}")
def buscar_aluno(id: int):
	db = SessionLocal()
	try:
		aluno = db.query(Aluno).filter(Aluno.id == id).first()
		if aluno is None:
			raise HTTPException(status_code=404, detail="Aluno não encontrado")
		return {
			"id": aluno.id,
			"nome": aluno.nome,
			"idade": aluno.idade
		}
	finally:
		db.close()

@router.put("/alunos/{id}")
def atualizar_aluno(id: int, aluno: AlunoCreate):
	db = SessionLocal()
	try:
		aluno_db = db.query(Aluno).filter(Aluno.id == id).first()
		if aluno_db is None:
			raise HTTPException(status_code=404, detail="Aluno não encontrado")
		aluno_db.nome = aluno.nome
		aluno_db.idade = aluno.idade
		db.commit()
		db.refresh(aluno_db)
		return {
			"id": aluno_db.id,
			"nome": aluno_db.nome,
			"idade": aluno_db.idade
		}
	finally:
		db.close()

@router.delete("/alunos/{id}")
def deletar_aluno(id: int):
	db = SessionLocal()
	try:
		aluno_db = db.query(Aluno).filter(Aluno.id == id).first()
		if aluno_db is None:
			raise HTTPException(status_code=404, detail="Aluno não encontrado")
		db.delete(aluno_db)
		db.commit()
		return {"detail": "Aluno deletado com sucesso"}
	finally:
		db.close()