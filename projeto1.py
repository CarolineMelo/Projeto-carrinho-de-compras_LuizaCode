
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from re import match


app = FastAPI()

OK = "OK"
FALHA = "FALHA"

# Classe representando os dados do endereço do cliente


class Endereco(BaseModel):
    id: int
    rua: str
    cep: str
    cidade: str
    estado: str

# Classe representando os dados do cliente


class Usuario(BaseModel):
    id: int
    nome: str
    email: str
    senha: str

# Classe representando a lista de endereços de um cliente


class ListaDeEnderecosDoUsuario(BaseModel):
    usuario: Usuario
    enderecos: List[Endereco] = []

# Classe representando os dados do produto


class Produto(BaseModel):
    id: int
    nome: str
    descricao: str
    preco: float

# Classe representando o carrinho de compras de um cliente com uma lista de produtos


class CarrinhoDeCompras(BaseModel):
    id_usuario: int
    id_produtos: List[Produto] = []
    preco_total: float
    quantidade_de_produtos: int


db_usuarios = {}
db_produtos = {}
db_end = {}        # todos os enderecos cadastrados
db_end_usr = {}        # enderecos_dos_usuarios
db_carrinhos = {}

# Essa função cadastra um usuário no sistema do "e-commerce".


@app.post("/usuario/")
async def criar_usuário(usuario: Usuario):
    if usuario.id in db_usuarios:
        return FALHA
    elif match(r"^[a-z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?(?:\.[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?)*$", usuario.email) and match(r"^[a-z0-9.!#$%&'*+@\/=?^_`{|}~-]{3,}$", usuario.senha):
        db_usuarios[usuario.id] = usuario
        return OK
    return FALHA

# Essa função traz um usuário por vez de acordo com o id.


@app.get("/usuario/{id}")
async def retornar_usuario(id: int):
    if id in db_usuarios:
        return db_usuarios[id]
    return FALHA

# Essa função traz todos os usuários que foram inseridos posteriormente.


@app.get("/usuarios")
async def retorna_usuarios():
    return db_usuarios

# Essa função traz o usuário cuja o nome for igual ao solicitado.


@app.get("/usuarios/nome")
async def retornar_usuario_com_nome(nome: str):
    for usuario in db_usuarios.values():
        if usuario.nome == nome:
            return usuario
    return FALHA

# Essa função serve para deletar o usuário.


@app.delete("/usuario/{id}/")
async def deletar_usuario(id: int):
    if id in db_usuarios:
        db_usuarios.pop(id)
        return OK
    return FALHA



@app.get("/")
async def bem_vinda():
    site = "Seja bem vinda"
    return site.replace('\n', '')
