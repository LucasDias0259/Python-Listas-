"""
exercício 2.5: Buscar Índice

Crie uma lista com nomes e:

1.Encontre a posição de "Carlos"
2.Encontre a posição de "Diana"
3.Verifique se "Zoe" existe antes de buscar

nomes = ["Alice", "Bob", "Carlos", "Diana", "Eduardo"]

# Seu código aqui
"""

nomes = ["alice","bob","carlos","diana","eduardo"]

posicao = nomes.index("carlos")
print(f"O Nome Carlos Está na lista de nomes na posição {posicao}")

posicao = nomes.index("diana")
print(f"O Nome Diana Está na lista de nomes na posição {posicao}")

if "zoe" in nomes:
    print(f"O Nome zoe está na lista de nomes")
else:
    print(f"O Nome zoe não esta na lista de nomes")