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
        # e será o somatório dos valores da carga
        self.nota_avaliacao = 0
        # espaço total usado neste carregamento
        self.espaco_usado = 0
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
                
    # função que vai avaliar se a solução é boa ou não
    def avaliação(self):
        nota = 0
        soma_espacos = 0
        
        for i in range(len(self.cromossomo)):
            if self.cromossomo[i] == "1":
                nota += self.valores[i]
                soma_espacos += self.espacos[i]
            if soma_espacos > self.limite_espacos:
                # apenas rebaixou a nota dos ruins para 1
                # para poder levar elas em considereção
                # é um padrão usar 1 quando trabalhar com algorimtos genéticos
                nota = 1
            self.nota_avaliacao = nota
            self.espaco_usado = soma_espacos
            
    def crossover(self, outro_individuo):
        # ponto de corte do cromossomo (número inteiro de 0 a 14)
        corte = round(random() * len(self.cromossomo))
        
        # [0:corte] da casa 0 até a casa (1 antes) do corte, [corte::] daí em diante
        # + concatena dois vetores - é o crossover
        filho1 = outro_individuo.cromossomo[0:corte] + self.cromossomo[corte::]
        filho2 = self.cromossomo[0:corte] + outro_individuo.cromossomo[corte::]
        
        # crio novos indivíduos com os dados dos pais (o que vai mudar é o cromossomo) obs: geração+1)
        filhos = [Individuo(self.espacos, self.valores, self.limite_espacos, self.geracao+1),
                  Individuo(self.espacos, self.valores, self.limite_espacos, self.geracao+1)]
        
        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2
        return filhos        
        
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
    
    # imprimindo indivíduo 1----------------------------------------------
    individuo1 = Individuo(espacos, valores, limite)
    print("\nIndivíduo 1")
   
    #contador de produtos levados
    cont = 1
    for i in range(len(lista_produtos)):
        if individuo1.cromossomo[i] == '1':
            print(f"{cont} Nome: {lista_produtos[i].nome} | Valor R${lista_produtos[i].valor:.2f}")
            cont += 1
            
    individuo1.avaliação()
    print(f"Nota = {individuo1.nota_avaliacao:.2f}")
    print(f"Espaço usado = {individuo1.espaco_usado:.2f}")
    
    
    # imprimindo indivíduo 2----------------------------------------------
    individuo2 = Individuo(espacos, valores, limite)
    print("\nIndivíduo 2")
   
    #contador de produtos levados
    cont = 1
    for i in range(len(lista_produtos)):
        if individuo2.cromossomo[i] == '1':
            print(f"{cont} Nome: {lista_produtos[i].nome} | Valor R${lista_produtos[i].valor:.2f}")
            cont += 1
            
    individuo2.avaliação()
    print(f"Nota = {individuo2.nota_avaliacao:.2f}")
    print(f"Espaço usado = {individuo2.espaco_usado:.2f}")
    
    individuo1.crossover(individuo2)