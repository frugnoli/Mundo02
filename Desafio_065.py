# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

num = soma = cont = maior = menor = 0
perg = 'S'
while perg != 'N':
    num = int(input("Digite um número: "))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    perg = str(input("Quer continuar ? [S/N] ")).upper().strip()[0]
media = (soma) / cont
print("Você digitou {} números e a média foi {:.2f}".format(cont, media))
print("O maior valor foi {} e o menor {}.".format(maior, menor))
    

