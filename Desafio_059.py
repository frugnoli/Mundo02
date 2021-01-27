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
opcao = 0
while opcao != 5:
    print("""
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    """)
    opcao = int(input(">>>>>> Qual é a sua opção: "))
    print("-=" * 20)
    if opcao == 1:
        print("A soma dos valores é {}".format(primeiro + segundo))
    elif opcao == 2:
        print("A multiplicação dos valores é {}".format(primeiro * segundo))
    elif opcao == 3:
        if primeiro > segundo:
            print("Primeiro valor é maior!")
        elif segundo > primeiro:
            print("Segundo valor é maior!")
        else:
            print("Valores iguais!")
    elif opcao == 4:
        primeiro = int(input("Primeiro Valor: "))
        segundo = int(input("Segundo Valor: "))
    elif opcao == 5:
        print("Finalisando . . .")
    else:
        print("Opção Inválida!")
    print("-=" * 20)
sleep(1)
print("FIM DO PROGRAMA, VOLTE SEMPRE!")
