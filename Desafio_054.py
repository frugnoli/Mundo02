# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
ano_atual = date.today().year
maior = menor = 0
for pessoa in range(1, 8):
    nasc = int(input("Em que ano a {}ª pessoa nasceu? ".format(pessoa)))
    nasc = ano_atual - nasc
    if nasc >= 21:
        maior += 1
    else:
        menor += 1
print("Ao todo tivemos {} pessoas de maior de idade e {} pessoas de menor de idade".format(maior, menor))


