# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
print("=" * 30)
print("10 TERMOS DE UMA PA")
print("=" * 30)
primeiro = int(input("Primeiro Termo: "))
razao = int(input("Razão: "))
pa = primeiro + (10 -1) * razao
for x in range(primeiro, pa + razao, razao):
    print("{}".format(x), end = ' -> ')
print("Acabou")