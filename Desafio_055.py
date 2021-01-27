# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = menor = 0
for x in range(1, 6):
    peso = float(input('Peso da {}ª Pessoa: '.format(x)))
    if x == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("O maior peso lido foi de {:.1f}Kg".format(maior))
print("O menor peso lido foi de {:.1f}Kg".format(menor))





