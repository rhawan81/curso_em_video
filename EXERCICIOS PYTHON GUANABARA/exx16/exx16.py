## importaçao do modulo trunc , ele quebra um numero com ponto flutuante e deixa ele inteiro
import math
from math import trunc
number = float(input("digite seu numero" \
""))

exibir_numero_inteiro = int(number) # pode ser usar desta maneira mais tambem pode inserir o math.trunc
print(f"seu numero é {number} ja a porção inteira é {exibir_numero_inteiro}")