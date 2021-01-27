# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
primeiro = int(input("Primeiro Valor: "))
segundo = int(input("Segundo Valor: "))
print("""
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa""")
opcao = int(input(">>>>>> Qual é a sua opção: "))
while opcao != 5:
    if opcao == 1:
        print("A soma dos resultados é {}".format(primeiro + segundo))
        print("-=" * 20)
print("Finalisando . . .")
print("-=" * 20)
sleep(1)
print("FIM DO PROGRAMA, VOLTE SEMPRE!")
