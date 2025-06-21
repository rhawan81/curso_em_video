from random import randint
import time
print("Vou pensar em um numero entre 0 e 5. tente advinhar....")
print("-=-" * 20)
computador = randint(1,5) # o Computador Sortear o numero 
usuario = int(input('Digite seu numero')) # jogador tenta advinhar
print("-=-" *20)
print("Processando....")
time.sleep(3)

if computador == usuario:
    print("Parabens meu numero foi {} e o seu foi {}".format(computador,usuario))

else:
    print('eu pensei no numero {} , ja voce pensou no {}'.format(computador,usuario))    