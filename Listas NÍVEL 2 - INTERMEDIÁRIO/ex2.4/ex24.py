"""
Exercício 2.4: Slicing

Crie uma lista com números de 0 a 9 e:

1.Imprima os primeiros 3 elementos
2.Imprima os últimos 3 elementos
3.Imprima cada 2º elemento
4.Imprima a lista invertida

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

"""

numeros = [0,1,2,3,4,5,6,7,8,9]
print(numeros[0:3]) 
print(numeros[7::]) # mostra o 1 ultimo elemento e mostra ate o ultimo elemento que e 9
print(numeros[0:-1:2])
print(numeros[::-1]) # colocando [::-1] mostra o inverso da lista o se quiser use .reverse() que mostra também o inverso da lista

