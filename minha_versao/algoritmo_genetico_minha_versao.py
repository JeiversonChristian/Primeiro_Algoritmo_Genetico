from random import random

# px: produto x
# Nome | Espaço que ocupa | valor do produto
p1 = ["Geladeira Dako", 0.751, 999.90]
p2 = ["Iphone 6", 0.0000899, 2199.12]
p3 = ["TV 55' ", 0.400, 4346.99]
p4 = ["TV 50' ", 0.290, 3999.90]
p5 = ["TV 42' ", 0.200, 2999.00]
p6 = ["Notebook Dell", 0.00350, 2499.90]
p7 = ["Ventilador Panasonic", 0.496, 199.90]
p8 = ["Microondas Electrolux", 0.0424, 308.66]
p9 = ["Microondas LG", 0.0544, 429.90]
p10 = ["Microondas Panasonic", 0.0319, 299.29]
p11 = ["Geladeira Brastemp", 0.635, 849.00]
p12 = ["Geladeira Consul", 0.870, 1199.89]
p13 = ["Notebook Lenovo", 0.498, 1999.90]
p14 = ["Notebook Asus", 0.527, 3999.00]
produtos = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14]

nomes = []
for i in range(len(produtos)):
    nomes.append(produtos[i][0])

espaco_limite = 3
espacos = []
for i in range(len(produtos)):
    espacos.append(produtos[i][1])

valores = []
for i in range(len(produtos)):
    valores.append(produtos[i][2])

populacao = 20

# c: cromossomo
c = []
cromossomos = []
for i in range(populacao):
    for j in range(len(produtos)):
        # random() - [0.0 a 1.0)
        if random() < 0.5:
            c.append(1)
        else:
            c.append(0)
    cromossomos.append(c)
    c = []

# n de nota: somatório dos valores dos produtos que vão no caminhão
n = 0
notas = []

# e_o de espaco_ocupado: somatório dos espaços dos produtos que vão no caminhão
e_o = 0
espacos_ocupados = []

for i in range(populacao):
    for j in range(len(produtos)):
        if cromossomos[i][j] == 1:
            e_o += espacos[j]
            n += valores[j]
    if e_o > espaco_limite:
        n = 1
    notas.append(n)
    n = 0
    espacos_ocupados.append(e_o)
    e_o = 0

print()
print("Produtos a serem levados de acordo com cada cromossomo:")
print("-------------------------------------------------------")
print()
for i in range(populacao):
    print(f"Cromossomo {i+1}:")
    for j in range(len(produtos)):
        if cromossomos[i][j] == 1:
            print(f"{nomes[j]} | {espacos[j]} | {valores[j]}")
    print(f"Espaço ocupado: {espacos_ocupados[i]} | Nota: {notas[i]}")
    print()
print("-------------------------------------------------------")
