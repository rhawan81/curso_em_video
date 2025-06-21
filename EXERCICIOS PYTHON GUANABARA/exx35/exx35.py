r1 = int(input())
r2 = int(input())
r3 = int(input())

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os segmentos acima podem montar o triangulo')

else:
    print('nao podem formar um triangulo')