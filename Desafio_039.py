# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
print("####### ALISTAMENTO MILITAR #######")
print("""Informe seu gênero, sendo que:
[ 1 ] - Masculino
[ 2 ] - Feminino""")
genero = str(input("Digite: "))
if genero == '1':
    nasc = int(input("Informe o ano do nascimento: "))
    ano_atual = date.today().year
    idade = ano_atual - nasc
    print("Quem nasceu em {} tem {} ano(s) em {}.".format(nasc, idade, ano_atual))
    if idade < 18:
        print("Ainda falta {} ano(s) para o alistamento.".format(18 - idade))
        print("Seu alistamento será em {}.".format(nasc + 18))
    elif idade > 18:
        print("Já deveria ter se alistado há {} ano(s).".format(idade - 18))
        print("Seu alistamento foi em {}.".format(nasc + 18))
    else:
        print("Você tem que se alistar IMEDIATAMENTE!")
elif genero == '2':
    print("Você não precisa se alistar!")
else:
    print("Opção inválida, tente novamente!")

