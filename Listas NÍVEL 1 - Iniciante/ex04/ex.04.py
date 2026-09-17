"""
Exercício 1.4: Verificar Existência

Crie uma lista com cores e:

1.Verificar se "vermelho" está na lista
2.Verificar se "azul" está na lista
3.Imprima mensagens apropriadas

cores = ["vermelho", "verde", "amarelo", "azul"]

# Seu código aqui

Saída esperada:

Vermelho está na lista
Azul está na lista

[v | a]
[0 | 0]
[0 | 1]
[1 | 0]
[1 | 1]

"""

cores = ["azul" ,"vermelho" , "verde" ,"amarelo"]
if "vermelho" not in cores and "azul" not in cores:
    print("Vermelho e Azul não estão na lista")
    print("False")
elif "vermelho" not in cores and "azul" in cores:
    print("Vermelho não esta na lista\nAzul está na lista")
    print("False and True")
elif "vermelho" in cores and "azul" not in cores:
    print("Vermelho está na lista\nAzul não esta na lista")
    print("True and False")
elif "vermelho" in cores and "azul" in cores:
    print("Vermelho e Azul estão na lista")
    print("True")

