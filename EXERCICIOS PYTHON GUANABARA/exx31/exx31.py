viagem = float(input('Qual a distancia da viagem ? '))
passagem = viagem * 0.50
print('Voce esta presta a começar uma viagem de {} km'.format(viagem))
if viagem <= 200:
    print('Voce ira pagar o total de : {}'.format(viagem * 0.50))

else:
    print('Voce ira pagar o total de {}'.format(viagem * 0.45))