# biblioteca para gerar números aleatórios
from random import random

# ------------------------------------------------------------------------------------------------------------
# Fazendo a lista de produtos do caminhão

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
# ------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------
# Fazendo vetores para guardarem as informações dos produtos

# guarda os nomes dos produtos
nomes = []
for i in range(len(produtos)):
    nomes.append(produtos[i][0])

# espaço limite interno do caminhão: 3m²
espaco_limite = 3

# guarda os espaços ocupados por cada produto
espacos = []
for i in range(len(produtos)):
    espacos.append(produtos[i][1])

# guarda os valores (R$) de cada produto
valores = []
for i in range(len(produtos)):
    valores.append(produtos[i][2])
# ------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------
# Fazendo uma população de cromossomos

# População: Quantidade de cromossomos
# Cromossomo: Sequência de bits que definem se um produto vai ou não no caminhão
populacao = 5
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
# ------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------
# Definindo a nota e o espaço ocupado de cada cromossomo

# n de nota: somatório dos valores dos produtos que vão no caminhão
n = 0
notas = []

# e_o de espaco_ocupado: somatório dos espaços dos produtos que vão no caminhão
e_o = 0
espacos_ocupados = []

for i in range(len(cromossomos)):
    for j in range(len(produtos)):
        if cromossomos[i][j] == 1:
            e_o += espacos[j]
            n += valores[j]
    # O espaço ocupado pelos produtos não pode exceder o limite
    if e_o > espaco_limite:
        n = 1
    notas.append(n)
    n = 0
    espacos_ocupados.append(e_o)
    e_o = 0
# ------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------
# Colocando os cromossomos, os espaços ocupados e as notas de cada um num único vetor

# c_e_n: [[cromossomos, espaços_ocupuados e notas]]
c_e_n = []
elemento_de_c_e_n = []
for i in range(len(cromossomos)):
    elemento_de_c_e_n.append(cromossomos[i])
    elemento_de_c_e_n.append(espacos_ocupados[i])
    elemento_de_c_e_n.append(notas[i])
    c_e_n.append(elemento_de_c_e_n)
    elemento_de_c_e_n = []
# ------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------
# Ordenando o vetor c_e_n

# "sorted()" é a função que ordena vetores
# "key=lambda elemento_de_c_e_n" é a referência para a ordenação
# Eu chamei de "elemento_de_c_e_n" os vetores que estão dentro do vetor c_e_n
# A referência, então, será os elementos da posição 2 desses vetores
# reverse=True é para colocar na ordem decrescente
c_e_n = sorted(c_e_n, key=lambda elemento_de_c_e_n: elemento_de_c_e_n[2], reverse=True)
# ------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------
# Imprimindo o vetor c_e_n (já ordenado)

print()
for i in range(len(c_e_n)):
    print(f"{c_e_n[i][0]} | {c_e_n[i][1]:.5f} m² | R$ {c_e_n[i][2]:.2f}")
# ------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------
# Imprimindo uma lista de produtos, com suas informações, a serem levados conforme o cromossomo

print()
print("Produtos a serem levados de acordo com cada cromossomo:")
print("-------------------------------------------------------")
print()
mensagem = "Espaço ocupado / Nota:"
for i in range(populacao):
    print(f"Cromossomo {i+1}:")
    for j in range(len(produtos)):
        # o cromossomo sempre será o elemento na posição 0 de cada elemento do vetor c_e_n
        if c_e_n[i][0][j] == 1:
            # .just() preenche o lado direito com espaços em branco - 22 é o tamanho ocupado total da string
            print(f"{nomes[j].ljust(22)} | {espacos[j]:.5f} m² | R$ {valores[j]:.2f}")
    print(f"{mensagem.ljust(22)} | {espacos_ocupados[i]:.5f} m² | R$ {notas[i]:.2f}")
    print()
print("-------------------------------------------------------")
# ------------------------------------------------------------------------------------------------------------
