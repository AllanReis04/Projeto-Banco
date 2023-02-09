import sqlite3
import random as r
from Bank import Banco
import json

bc = Banco()
print("(c) Criar Conta")
print("(a) Acessar Conta")
op = input("Digite o que deseja acessar: ")

if op == 'a' or op == 'A':
    bc.AcessarConta()
elif op == 'c' or 'C':
    bc.CriarConta()

