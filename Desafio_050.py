# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for x in range(1, 7):
    numeros = int(input(("Digite o {} valor: ".format(x))))
    if numeros % 2 == 0:
        soma += numeros
        cont += 1
print("Você informou {} números pares e a soma foi {}".format(cont, soma))