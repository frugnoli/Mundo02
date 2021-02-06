# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra (t).
# B) quantos produtos custam mais de R$1000 (p).
# C) qual é o nome do produto mais barato (b,n).
print("{:-^40}".format(" LOJA BARATÃO "))
t = p = menor = cont = 0
nomeprod = ''
while True:
    prod = str(input("Nome do Produto: ")).upper()
    preco = float(input("Valor: R$ "))
    t += preco
    cont += 1
    if preco > 1000:
        p += 1
    if cont == 1 or preco < menor:
        menor = preco
        nomeprod = prod
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    if opcao == 'N':
        break
print(f"O total em compras foi de R${t:.2f}.")
print(f"Houve {p} produtos que custaram mais de R$1000.00")
print(f"O produto mais barato foi o {nomeprod} que custou {menor:.2f}.")
print("{:-^40}".format(" FIM DO PROGRAMA "))