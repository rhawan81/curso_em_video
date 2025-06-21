peso = int(input('Qual é seu peso ? (kg)'))
altura = float(input('Qual sua Altura ? (m)'))

imc = peso / (altura ** 2)
print('SEU IMC É {:.1f}'.format(imc))
if imc <= 18.5:
    print('ABAIXO DO PESO')

elif imc >= 18.5 and imc < 25:
    print('PESO IDEAL')

elif imc > 25 and imc < 30:
    print('SOBREPESO')

elif imc > 30 and imc <= 40:
    print('OBESIDADE')

else:
    print('OBESIDADE MORBIDA')              