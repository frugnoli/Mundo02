# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
num = int(input("Digite um número para\ncalcular seu Fatorial: "))
c = num
f = 1
print("Calculando o Fatorial de {}! -> ".format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
    
print("{}".format(f))

# pode ser usado o de baixo...

# from math import factorial
# num = int(input("Digite um número para\ncalcular seu Fatorial: "))
# f = factorial(num)
# print("Calculando o Fatorial de {}! é {}.".format(num, f))
