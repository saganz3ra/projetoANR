from Cachorro import Cachorro
from Gato import Gato
from Servico import Servico
from Info import Info

def bem_vindo():
    print("==========================================================")
    print("Olá sejá bem vindo ao ANR Pet!")
    print("O melhor cuidado para seu Pet!")
    print("==========================================================")

# EXECUÇÃO PRINCIPAL

s1 = Servico(0)

bem_vindo()
s1.servico()

print("==========================================================")
print("Agora vamos começar o atendimento!")
print("==========================================================\n")

especie = input("Digite qual é a especie de seu animal: ")
raca = input(f"Digite a raca de seu {especie}: ")
nome = input(f"Digite o nome do seu {especie}: ")
cor = input(f"Qual a cor de seu {especie}: ")
idade = input(f"Qual a idade de seu {especie}: ")
vacinas = input(f"Quantas vacinas seu {especie} ja tomou? ")
s1.pausar()

especie = especie.upper()
raca = raca.upper()
nome = nome.upper()

if especie == "CACHORRO":

    especie = especie.lower()
    raca = raca.lower()
    nome = nome.lower()

    # PARA SERVIÇO DE CORTAR AS GARRAS
    garra = input("Deseja cortar as unhas do seu cachorro? ")
    garra = garra.upper()
    if garra == "SIM":
        s1.cortar_garra()
        print("Serviço incluso!")
    s1.pausar()

    # IF PARA CORTAR O PELO
    pelo = input("Você deseja tosar seu cachorro? ")
    pelo = pelo.upper()
    if pelo == "SIM":
        quanto_cortar = input("Deseja deixar o pelo de seu cachorro na altura alta, media ou baixa? ")
        print("Serviço incluso!")
        s1.tosar()
    s1.pausar()

    # IF PARA O BANHO
    banho = input("Você deseja dar banho em seu cachorro? ")
    banho = banho.upper()
    if banho == "SIM":
        s1.banhar()
        print("Serviço incluso!")

    s1.pausar()

    # IF PARA PASSEAR
    passear = input("Você deseja passear com seu cachorro? ")
    passear = passear.upper()
    if passear == "SIM":
        s1.passear()
        print("Serviço incluso!")
    s1.pausar()

    c1 = Cachorro(especie, raca, nome, cor, idade, vacinas, pelo, garra)

    # PARA INFORMAR OS DADOS SOBRE O ANIMAL
    i1 = Info(especie, raca, nome, cor, idade)
    i1.dados()

    i1 = Info(especie, raca, nome, cor, idade)
    i1.abrir_arquivo(pelo, banho, passear, garra)

if especie == "GATO":

    especie = especie.lower()
    raca = raca.lower()
    nome = nome.lower()
    cor = cor.lower()

    # PARA SERVIÇO DE CORTAR AS GARRAS
    garra = input("Deseja cortar as unhas do seu gato? ")
    garra = garra.upper()
    if garra == "SIM":
        s1.cortar_garra()
        print("Serviço incluso!")
    s1.pausar()

    pelo = input("Você deseja tosar seu gato? ")
    pelo = pelo.upper()

    # IF PARA CORTAR O PELO
    if pelo == "SIM":
        quanto_cortar = input("Deseja deixar o pelo de seu gato na altura, alta, media ou baixa? ")
        print("Serviço incluido!")
        s1.tosar()
    s1.pausar()

    # IF PARAR O BANHO
    banho = input("Você deseja dar banho em seu gato? ")
    banho = banho.upper()
    if banho == "SIM":
        s1.banhar()
        print("Serviço incluido!")
    s1.pausar()

    passear = input("Você deseja passear com seu gato? ")
    passear = passear.upper()
    if passear == "SIM":
        s1.passear()
        print("Serviço incluido!")
    s1.pausar()

    g1 = Gato(especie, raca, nome, cor, idade, pelo, garra)

    # PARA INFORMAR OS DADOS SOBRE O ANIMAL
    i1 = Info(especie, raca, nome, cor, idade)
    i1.dados()

    i1 = Info(especie, raca, nome, cor, idade)
    i1.abrir_arquivo(pelo, banho, passear, garra)

print("==========================================================")
print("Atendimento finalizado, volte sempre!")
print("==========================================================\n")
s1.nota()