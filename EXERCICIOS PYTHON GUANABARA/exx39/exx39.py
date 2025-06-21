from datetime import date

ano_nascimento = int(input('Ano de Nascimento ? '))
atual = date.today().year
idade = atual - ano_nascimento
print('Quem Nasceu No ano de {} tem {} anos em {}'.format(ano_nascimento,idade,atual))

if idade == 18:
    print('Voce tem que alistar IMEDIATAMENTE !')

elif idade < 18:
    saldo = 18 - idade
    print(' Ainda falta {} anos para o alistamento'.format(saldo)) 
    ano = atual + saldo

elif idade > 18:
    saldo = idade - 18
    print('Voce ja deveria ter se alistado ha {} anos '.format(saldo)) 
    ano = atual - saldo


print('seu alistamento sera em {}'.format(ano))         