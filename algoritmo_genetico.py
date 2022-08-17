# importação da função random que gera números aleatórios entre 0 e 1
from random import random

# cada produto será um objeto desta classe
class Produto():
    def __init__(self, nome, espaco, valor):
        self.nome = nome
        self.espaco = espaco
        self.valor = valor

# um indivíduo é uma lista de produtos        
class Individuo():
    def __init__(self, espacos, valores, limite_espacos, geracao=0):
        self.espacos = espacos
        self.valores = valores
        self.limite_espacos = limite_espacos
        # cada indivíduo etá uma nota para saber se é bom ou não
        self.nota_avaliacao = 0
        self.geracao = geracao
        # cromossomo será preechido por soluções representadas por 0's e 1's
        self.cromossomo = []
        
        # preenchendo aleatoriamente o cromossomo
        # cromossomo terá o tamanho igual à quantidade de produtos
        # como cada um ocupa um espaço, basta saber quantos espaços são
        for i in range(len(espacos)):
            # 50% de probabilidade
            if random() < 0.5:
                self.cromossomo.append("0")
            else:
                self.cromossomo.append("1")
        
if __name__ == '__main__':
    
    # criando cada (objeto produto) da (classe Produto)
    # px: produto x
    # Nome | Espaço que ocupa | valor do produto
    
    p1 = Produto("Geladeira Dako", 0.751, 999.90)
    p2 = Produto("Iphone 6", 0.0000899, 2199.12)
    p3 = Produto("TV 55' ", 0.400, 4346.99)
    p4 = Produto("TV 50' ", 0.290, 3999.90)
    p5 = Produto("TV 42' ", 0.200, 2999.00)
    p6 = Produto("Notebook Dell", 0.00350, 2499.90)
    p7 = Produto("Ventilador Panasonic", 0.496, 199.90)
    p8 = Produto("Microondas Electrolux", 0.0424, 308.66)
    p9 = Produto("Microondas LG", 0.0544, 429.90)
    p10 = Produto("Microondas Panasonic", 0.0319, 299.29)
    p11 = Produto("Geladeira Brastemp", 0.635, 849.00)
    p12 = Produto("Geladeira Consul", 0.870, 1199.89)
    p13 = Produto("Notebook Lenovo", 0.498, 1999.90)
    p14 = Produto("Notebook Asus", 0.527, 3999.00)

    # colocando cada classe Prduto em uma lista    
    lista_produtos = []
    
    lista_produtos.append(p1)
    lista_produtos.append(p2)
    lista_produtos.append(p3)
    lista_produtos.append(p4)
    lista_produtos.append(p5)
    lista_produtos.append(p6)
    lista_produtos.append(p7)
    lista_produtos.append(p8)
    lista_produtos.append(p9)
    lista_produtos.append(p10)
    lista_produtos.append(p11)
    lista_produtos.append(p12)
    lista_produtos.append(p13)
    lista_produtos.append(p14)
    
    #for produto in lista_produtos:
        #print(produto.nome)
    
    # listas para guardar os dados dos produtos
    nomes = []
    espacos = []
    valores = []
    
    # preenchendo as listas com os dados dos produtos
    for produto in lista_produtos:
        nomes.append(produto.nome)
        espacos.append(produto.espaco)
        valores.append(produto.valor)
    
    # limite de espaço do caminhão: 3m³
    limite = 3
    
    individuo1 = Individuo(espacos, valores, limite)
    print(f"Espaços = {str(individuo1.espacos)}")
    print(f"Valores = {str(individuo1.valores)}")
    print(f"Cromossomo = {str(individuo1.cromossomo)}")
    print()
    print("Produtos que serão carregados:")
    for i in range(len(lista_produtos)):
        if individuo1.cromossomo[i] == '1':
            print(f"Nome: {lista_produtos[i].nome} | Valor R${lista_produtos[i].valor:.2f}")