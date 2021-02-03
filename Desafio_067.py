# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.


while True:
    print("-" * 50)
    num = int(input("Quer ver a tabuada de qual valor? "))
    print("-" * 50)
    if num < 0:
        break
    else:
        for c in range(0, 11):
            print(f"{num} x {c} = {num * c}") 
print("PROGRAMA DE TABUADA ENCERRADO. VOLTE SEMPRE!\n")
 