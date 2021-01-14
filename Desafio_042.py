# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

print("-=-" * 10)
print("Analisador de Triângulos")
print("-=-" * 10)
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
print("-=-" * 10)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima, podem formar um triângulo ", end="")
    if r1 == r2 == r3:
        print("EQUILÁTERO!")
    if r1 != r2 != r3 != r1:
        print("ESCALENO!")
    else:
        print("ISÓSCELES!")
else:
    print("Os segmentos NÃO podem formar um triângulo!")

