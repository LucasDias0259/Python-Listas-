"""
Exercício 2.3: Ordenar Lista

Crie uma lista com números desordenados e:

1.Ordene em ordem crescente e imprima
2.Ordene em ordem decrescente e imprima
3.Inverta a lista e imprima

numeros = [5, 2, 8, 1, 9, 3]

# Seu código aqui

"""

numeros = [5,2,8,1,9,3]
numeros.sort()
print(f"Crescente: {numeros}")
numeros.reverse()
print(f"Decrescente: {numeros}")
numeros = [5,2,8,1,9,3]
numeros.reverse()
print(f"Invertida: {numeros}")

