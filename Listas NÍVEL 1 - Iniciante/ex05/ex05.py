"""
Exercício 1.5: Remover Elementos

Crie uma lista com 5 nomes e:

1.Remova o segundo nome
2.Imprima a lista
3.Remova o último nome
4.Imprima a lista novamente

nomes = ["Alice", "Bob", "Carlos", "Diana", "Eduardo"]

# Seu código aqui

Saída esperada:

['Alice', 'Carlos', 'Diana', 'Eduardo']
['Alice', 'Carlos', 'Diana']

"""


nomes = ["alice","bob","carlos","diana","eduardo"]
nomes.remove(nomes[1])
"""
retirando pelo indice lista.remove(lista[posição_da_lista])

1.Remova o segundo nome
2.Imprima a lista
3.Remova o último nome
4.Imprima a lista novamente

"""
print(nomes)
nomes.remove(nomes[-1])
print(nomes)

