# Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
print("=-" * 30)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("=-" * 30)
v = 0
while True:
    jogador = int(input("Diga um valor: "))
    computador = randint(0, 10)
    opcao = ' '
    soma = jogador + computador
    while opcao not in 'PI':
        opcao = str(input("Par ou Ímpar [P/I] ")).strip().upper()[0]
        print("-" * 60)
    print(f"Você jogou {jogador} e o computador {computador}. Total de {soma} ", end='')
    print("DEU PAR" if soma % 2 == 0 else "DEU ÍMPAR")
    if opcao == 'P':
        if soma % 2 == 0:
            print("Você VENCEU!")
            v += 1
        else:
            print("VOCÊ PERDEU!")
            break
    elif opcao == 'I':
        if soma % 2 == 1:
            print("VOCÊ VENCEU!")
            v += 1
        else:
            print("VOCÊ PERDEU!")
            break
    print("Vamos jogar novamente...")
    print("-" * 60)
print("=-" * 30)
print(f"GAMER OVER! Você venceu {v} vez(es).")     
print("=-" * 30)
         