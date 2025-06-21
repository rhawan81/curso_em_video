number = int(input('Digite um Numero Inteiro'))
print("""Escolha uma das bases para conversão :
    [1] converter para BINARIO
    [2] Converter para OCTAL
    [3] Converter para HEXADECIMAL""")
    

opcao= int(input("escolha uma opçao"))

if opcao == 1:
    print('O VALOR EM BINARIO É : {}'.format(bin(number)[2:]))
elif opcao == 2:
    print('O VALOR EM OCTAL É :{}'.format(oct(number)[2:]))

elif opcao == 3:
    print('O VALOR EM HEXADECIMAL É:{}'.format(hex(number)[2:]))