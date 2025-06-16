import random
# str é uma boa pratica para passar para string apos o usuario digitar no input
person1 = str(input("digite seu nome"))
person2 = str(input("digite seu nome"))
person3 = str(input("digite seu nome"))
person4 = str(input("digite seu nome"))

lista = [person1,person2,person3,person4]
random.shuffle(lista)
print("A ordem da apresentação será :")
print(lista)