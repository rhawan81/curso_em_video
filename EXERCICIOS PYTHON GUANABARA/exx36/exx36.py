valor_casa = float(input('Valor da Casa em R$:'))
salario_person = float(input('Qual o valor do seu salario ? '))
anosA_pagar = int(input('Voce ira Pagar em quantos anos'))

prestaçao = valor_casa / (anosA_pagar * 12)
minimo = salario_person * 30 / 100
print('Para pagar uma casa de {:.2f} em {} anos , a prestação sera de {:.2f}'.format(valor_casa,anosA_pagar,prestaçao))
if prestaçao <= minimo:
    print('EMPRESTIMO APROVADO')
else:
     print('EMPRESTIMO NEGADO')


