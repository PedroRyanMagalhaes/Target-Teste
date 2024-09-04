string = input("Digite uma string:  ")

contagem_a = string.count("a")
contagem_A = string.count("A")

totalContagem = contagem_A + contagem_a

if totalContagem > 0:
    print (f"Na string existem {totalContagem} a ou A")
else:
    print (f"Não existem a ou A na string")