from clientes import cliente 
from contas import conta
import os

Cliente = cliente
Conta = conta

# imprime na tela 
print("*************************")
print("BEM VINDO AO BANCO INTER ")
print("*************************")
print()

print("Vamos criar a sua conta: ")

# entrada dos dados do cliente
cliente.nome = input("Digite o seu nome: ")
cliente.cpf = float(input("Digite seu cpf: "))
cliente.idade = int(input("Digite sua idade: "))
conta.limite = float(input("Digite um limite para sua conta: "))

# imprime os dados 
print("Nome: ", cliente.nome)
print("CPF: ", cliente.cpf)
print("Idade: ", cliente.idade)
os.system("cls")

# faz o saque / deposito na conta 
# pode ser alterado no futuro e melhorado a lógica 

print("DEPOSITAR, SACAR E VERIFICAR SALDO ")
conta.depositar = float(input("Digite o valor a ser depositado: "))
conta.saldo = 2000
print("Saldo: ", conta.saldo)
conta.saldo += conta.depositar
print(conta.saldo)
conta.sacar = float(input("Digite a quantidade para sacar: "))
print("Saldo: ", conta.saldo)
conta.saldo -= conta.sacar
print(conta.saldo)



