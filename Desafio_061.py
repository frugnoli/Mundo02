# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print("=" * 30)
print("GERADOR DE PA")
print("=" * 30)
primeiro = int(input("Primeiro Termo: "))
razao = int(input("Razão da PA: "))
termo = primeiro
contador = 1
while contador <= 10:
    print("{} -> ".format(termo), end = '')
    termo += razao
    contador += 1
print("Acabou")