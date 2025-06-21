nota1 = float(input('Primeira nota '))
nota2 = float(input('Segunda Nota'))

media = (nota1 + nota2 ) / 2

if media >= 7 and media > 5:
    print('AlUNO COM NOTA {:.1f} APROVADO'.format(media))

else:
    print('ALUNO DE NOTA {:.1f} ESTA  REPROVADO' .format(media))        