from datetime import date
# importaçao da biblioteca datetime ou seja ela pega a data atual e o ano se o usuario digitar 0 ele ira verificar as condições
ano = int(input('Que ano voce quer Analisar '))
if ano == 0:
    ano = date.today().year

    # o ano vai ser bissexto se seguir os seguintes requisitos , ser divisivel por  4 , 100 e 400 caso nao ocorra isso ele nao sera bissexto


if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('seu ano de {} bissexto'.format(ano))

else:
    print('O Ano {} Não é bissexto'.format(ano))    