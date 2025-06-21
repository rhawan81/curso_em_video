num1 = int(input('PRIMEIRO SEGMENTO'))
num2 = int(input('SEGUNDO SEGMENTO'))
num3 = int(input('TERCEIRO SEGMENTO'))

if num1 == num2 and num3 == num2:
    print('TRIANGULO EQUILATERO')

elif num1 != num2 and num3 != num2 and num1 != num3:
    print('ESCALENO')

else:
    print('ISOSCELES')