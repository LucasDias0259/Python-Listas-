"""
NÍVEL 2 - INTERMEDIÁRIO
Exercício 2.1: Iterar e Imprimir

Crie uma lista com números de 1 a 5 e:

numeros = [1, 2, 3, 4, 5]

1.Use um loop para imprimir cada número multiplicado por 2
2.Use enumerate() para imprimir também a posição

# Seu código aqui
"""

numeros = [1,2,3,4,5]
for i , v in enumerate(numeros):
    print(f"Posição {i}: {v} * 2 = {v*2}")

