frase = str(input("digite uma frase")).strip().upper()

print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A letra A apareceu na posição {}'.format(frase.find('A') + 1))
#rfind procura algum item na direita da frase 
#  O +1 faz a "tradução" entre o índice do computador e a posição que uma pessoa espera ler
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))