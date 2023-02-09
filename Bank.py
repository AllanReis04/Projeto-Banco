import sqlite3
import random as r
import json
class Banco:
    print("Bem-vindo ao Banco")

    def __init__(self):

        self.con = sqlite3.connect("Bank.db")
        self.c = self.con.cursor()

    def CriarConta(self):
        self.c.execute("""create table if not exists Bank
                    (
                        nome_conta text,
                        acc_num integer,
                        saldo integer
                    )""")

        nome1 = input("Digite o seu primeiro nome: ").upper()
        nome2 = input("Digite o seu sobrenome: ").upper()


        if nome1.isalpha() and not nome1.isspace() and nome2.isalpha() and not nome2.isspace():
            nome = nome1 + ' ' + nome2
            num = r.randint(10000000, 99999999)
            saldo = 0
            self.c.execute("insert into Bank Values(?,?,?)", (nome, num, saldo))
            print("{}, Sua conta foi criada com sucesso!".format(nome))
            print("O numero da conta é {}".format(num))
            self.con.commit()
            self.con.close

        else:
            print("Digite um nome valido!")
            
    def AcessarConta(self):
        a_num = int(input("Digite o numero da conta: "))
        check = True
        flag = False
        for a, b, c in self.c.execute("select * from Bank"):
            if b == a_num:
                check = False
                flag = True
                val = c
                na = a
                print("-"*50)
                print("(d)-Depositar")
                print("(s)-Sacar")
                print("(i)-Informações da Conta")
                print("(r)-Remover a Conta")               
                dsc = input(" Digite uma das operações (d), (s), (c) (r): ")
                '''default = 'r', 'R', 'i', 'I', 's', 'S', 'd', 'D'
                if dsc != default:
                    print("Alternativa inválida!")'''
                print("-"*50)
                
        if flag and (dsc == 'd' and 'D'):
            dep = int(input("Digite a quantidade que irá depositar: "))
            deposito = dep + val
            self.c.execute("update Bank set saldo = ? where acc_num = ?", (deposito, a_num))
            self.con.commit()
            print("Quantidade depositada R${}, saldo atual é de R${}".format(dep, deposito))
            self.con.close()
        if flag and (dsc == 's' or dsc == 'S'):
            wit = int(input("Digite a quantidade que deseja sacar: "))
            if val > 0 and val >= wit:
                saque_bal = val - wit
                self.c.execute("update Bank set saldo = ? where acc_num = ?", (saque_bal, a_num))
                self.con.commit()
                print("Saque de R${}, feito com sucesso! Saldo total de R${}".format(wit, saque_bal))
                self.con.close()
            else:
                print("Saldo Negativo")
        if flag and (dsc == 'r' or dsc == 'R'):
            self.c.execute(f"DELETE FROM Bank WHERE acc_num = ?", (a_num,))
            print("Sua conta foi removida com sucesso")
            self.con.commit()


        if flag and (dsc == 'i' or dsc == 'I'):
            
            dados = {
                'Nome da Conta': na,
                'Numero de Acesso': a_num,
                'Saldo Total': val
                }   
            jsonTest = json.dumps(dados, indent = 4)
            print(jsonTest)
            
        if check:
            print("Numero da conta inválido!")