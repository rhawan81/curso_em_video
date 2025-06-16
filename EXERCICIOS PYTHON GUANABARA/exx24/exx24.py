cidade = str(input("Em que Cidade Voce Nasceu ? ")).strip()
# O :5 mostra toda a string da cidade ou seja retorna um valor apos isso ele e convertido para maiusculo quando o usuario digita, se for igual a santo retornara True caso nao False
print(cidade[:5].upper() == 'SANTO')