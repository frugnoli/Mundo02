# Crie um programa que faça o computador jogar Jokenpô com você.
from time import sleep
from random import randint
itens = ("PEDRA", "PAPEL", "TESOURA")
computador = randint(0, 2)

print("\n{:=^60}".format(" \033[1;31mJO""\033[m\033[1;32mKEN""\033[1;31mPÔ ""\033[m"))
print(""" 
Suas opções:

[\033[1;31m 0\033[m ] PEDRA
[\033[1;31m 1\033[m ] PAPEL
[\033[1;31m 2\033[m ] TESOURA
""")
jogador = int(input("Qual é a sua jogada:\033[1;31m "))
sleep(0.5)
print("\033[1;31mJO\033[m")
sleep(0.5)
print("\033[1;32mKEN\033[m")
sleep(0.5)
print("\033[1;31mPÔ\033[m")
print("=-" * 20)
print("COMPUTADOR jogou {}".format(itens[computador]))
print("=-" * 20)
print("JOGADOR jogou {}".format(itens[jogador]))
print("=-" * 20)
if computador == 0:
    if jogador == 0:
        print("\nEMPATE\n")
    elif jogador == 1:
        print("\nCOMPUTADOR VENCEU\n")
    elif jogador == 2:
        print("\nJOGADOR VENCEU\n")
    else: 
        print("\nOPÇÃO INVÁLIDA\n")
elif computador == 1:
    if jogador == 0:
        print("\nCOMPUTADOR VENCEU\n")
    elif jogador == 1:
        print("\nEMPATE\n")
    elif jogador == 2:
        print("\nJOGADOR VENCEU\n")
    else: 
        print("\nOPÇÃO INVÁLIDA\n")
elif computador == 2:
    if jogador == 0:
        print("\nJOGADOR VENCEU\n")
    elif jogador == 1:
        print("\nCOMPUTADOR VENCEU\n")
    elif jogador == 2:
        print("EMPATE\n")
    else: 
        print("OPÇÃO INVÁLIDA\n")
