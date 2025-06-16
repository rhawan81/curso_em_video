### manipulando strings
nome = str(input("digite seu nome")).strip()
print('seu nome em maiusculo é {}'.format(nome.upper()))

print('seu nome em minusculo é {}'.format(nome.lower()))

print('seu nome tem ao todo {}'.format(len(nome) - nome.count(' ')))

print('seu primeiro nome é {}'.format(nome.find(' ')))

