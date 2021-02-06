# Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
h = p = m = 0
while True:
    idade = int(input("Idade: "))
    if idade > 18:
        p += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
        if sexo == 'M':
            h += 1
        if sexo == 'F' and idade < 20:
            m += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input("Quer continuar [S/N]: ")).strip().upper()[0]
    if resp == 'N':
        break
print(f"Total de {p} pessoas com mais de 18 anos")
print(f"Total de {h} homens cadastrados")
print(f"Total de {m} mulheres com menos de 20 anos")  