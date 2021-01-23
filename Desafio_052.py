# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um número: '))
total = 0
for x in range(1, num + 1):
    if num % x == 0:
        print('\033m[33m', end='')
        total += 1
    else:
        print('\033m[31m', end='')
    print("{}".format(x), end=' ')
print("\n\033[mO número {} foi divisível {} vezes".format(num, total))
if total == 2:
    print("E por isso ele é um número PRIMO!")
else:
    print("E por isso ele NÃO é um número PRIMO!")

