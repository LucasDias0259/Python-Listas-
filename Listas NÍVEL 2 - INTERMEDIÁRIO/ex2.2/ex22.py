"""
Exercício 2.2: Contar Ocorrências

Crie uma lista com números repetidos e:

1.Conte quantas vezes o número 5 aparece
2.Conte quantas vezes o número 3 aparece
3.Imprima os resultados

numeros = [1, 5, 3, 5, 5, 3, 7, 5, 2, 3]

# Seu código aqui
"""
numeros = [1,5,3,5,5,3,7,5,2,3]

contador = numeros.count(5)
print(f"O número 5 aparece {contador} vezes")
contador = numeros.count(3)
print(f"O número 3 aparece {contador} vezes")