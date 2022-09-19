
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

