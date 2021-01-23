# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
tab = int(input("Informe o número: "))
for x in range(1, 11):
    print('{} x {:2} = {}'.format(tab, x, tab * x))
print("=" * 100)

