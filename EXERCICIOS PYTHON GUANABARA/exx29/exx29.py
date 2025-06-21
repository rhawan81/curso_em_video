velocidade = int(input("Qual a Velocidade do seu carro ? "))
multa = (velocidade - 80 ) * 7

if velocidade <= 30:
    print("Tenha um bom dia , dirija com segurança!")

elif velocidade > 80:
    print('Voce foi mutado por transitar rapido demais')

print('Sua multa é de {} Reais'"\n".format(multa))