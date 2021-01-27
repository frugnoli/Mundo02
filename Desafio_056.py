# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulhermenos20 = 0
for x in range(1, 5):
    print("------ {}ª PESSOA ------".format(x))
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: "))
    somaidade += idade
    if x == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem: 
        maioridadehomem = idade
        nomevelho = nome
    if idade < 20 and sexo in 'Ff':
        mulhermenos20 += 1 
mediaidade = somaidade / 4
print("A média de idade do grupo é de {} anos".format(mediaidade))
print("O homem mais velho se chama {} e tem {} anos".format(nomevelho, maioridadehomem))
print("Ao todo são {} mulheres com menos de 20 anos".format(mulhermenos20))
