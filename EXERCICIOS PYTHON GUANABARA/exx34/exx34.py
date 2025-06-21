salario = int(input('Digite seu salario'))
aumento_inferior = salario + (salario * 0.15)
aumento_superior = salario +(salario * 0.10)

if salario > 1250:
    print('Seu salario era {} e passou a ser {}'.format(salario,aumento_superior))
elif salario < 1250:
    print('Seu salario era de {} e teve o aumento de {}'.format(salario,aumento_inferior))
