from fastapi import FastAPI  # Importa o FastAPI corretamente
from app.database import engine, SessionLocal, Base  # Importa objetos do banco
from app.models import Aluno  # Importa o modelo Aluno
from app.schemas import AlunoCreate  # Importa o schema de criação
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()  # Instancia o app FastAPI

# Cria as tabelas no banco de dados, se não existirem
Base.metadata.create_all(bind=engine)

# Endpoint de health check para saber se a API está online
from fastapi import FastAPI  # Importa o FastAPI corretamente
from app.database import engine, SessionLocal, Base  # Importa objetos do banco
from app.models import Aluno  # Importa o modelo Aluno
from app.schemas import AlunoCreate  # Importa o schema de criação
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

# ===================== OBSERVAÇÕES IMPORTANTES =====================
#
# 1. Se você acessar http://127.0.0.1:8000 e ver {"detail": "Not Found"},
#    isso é normal! Não existe rota para a raiz ("/").
#
# 2. Para testar se a API está funcionando, acesse:
#    - http://127.0.0.1:8000/health  (deve retornar {"status": "ok"})
#    - http://127.0.0.1:8000/docs    (documentação interativa do FastAPI)
#
# 3. O erro "ModuleNotFoundError: No module named 'database'" foi resolvido
#    corrigindo o import em models.py para 'from app.database import Base'.
#
# 4. Se aparecer erro 404 em outras rotas, verifique se o endpoint existe.
#
# 5. Sempre rode o servidor com:
#    uvicorn app.main:app --reload
# ===================================================================

app = FastAPI()  # Instancia o app FastAPI

# Cria as tabelas no banco de dados, se não existirem
Base.metadata.create_all(bind=engine)

# Endpoint de health check para saber se a API está online
@app.get("/health")
def health():
    return {"status": "ok"}

# Endpoint para criar um novo aluno
@app.post("/alunos")
def criar_aluno(aluno: AlunoCreate):
    db = SessionLocal()  # Cria uma sessão com o banco de dados
    try:
        # Cria um novo objeto Aluno a partir dos dados recebidos
        novo_aluno = Aluno(
            nome=aluno.nome,
            idade=aluno.idade
        )
        db.add(novo_aluno)  # Adiciona o aluno à sessão
        db.commit()  # Salva as alterações no banco
        db.refresh(novo_aluno)  # Atualiza o objeto com o ID gerado
        # Retorna os dados do novo aluno em formato JSON
        return JSONResponse(content=jsonable_encoder({
            "id": novo_aluno.id,
            "nome": novo_aluno.nome,
            "idade": novo_aluno.idade
        }))
    finally:
        db.close()  # Fecha a sessão do banco de dados

# Endpoint para listar todos os alunos
@app.get ("/alunos")
def listar_alunos():
    db = SessionLocal() #ABRE A SESSÃO COM O BANCO DE DADOS (cria conexão com o banco)
    try:
        alunos = db.query(Aluno).all() #CONSULTA TODOS OS ALUNOS NO BANCO DE DADOS E ARMAZENA NA VARIÁVEL "alunos"

        return JSONResponse(
            content=jsonable_encoder(alunos)
        )
    
    finally:
        db.close()