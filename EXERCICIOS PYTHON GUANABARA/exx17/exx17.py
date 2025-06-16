import math

cateto_oposto = float(input("comprimento do cateto oposto"))

cateto_adjacente = float(input("comprimento do cateto adjacente"))
# metodo usado foi hypot ou seja ele faz a função de me retornar o resultado da hipotenusa
hipotenusa = math.hypot(cateto_oposto , cateto_adjacente)

# no print implementei o metodo trunc ou seja ele ira retornar inteiro 
print(math.trunc(hipotenusa))