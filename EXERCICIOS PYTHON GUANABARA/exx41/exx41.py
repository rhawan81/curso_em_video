from datetime import date
nascimento = int(input('Ano de Nascimento :'))
atual = date.today().year
idade = atual - nascimento

print(f"tem a idade de {idade}")

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')    

elif idade <= 19:
    print('JUNIOR')

elif idade >= 25:
    print('SENIOR')

else:
    print('MASTER')