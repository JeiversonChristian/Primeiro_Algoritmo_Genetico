# Algoritmo do Caminhão (Aceito sugestões de nomes)


# --------------------------------------------------------------------------------------------------------------------
# Bibliotecas

# Biblioteca que gera números aleatórios
# não precisa instalar
import random

# Biblioteca usada para gerar gráfico
# Para instalar no windons cmd: pip install matplotlib
import matplotlib.pyplot as plt

# Biblioteca que conecta ao banco de dados do mysql
# Para instalar no windons cmd: pip install mysql
from mysql.connector import connect

# Blioteca pra fazer alguns cálculos
# não precisa instalar
import numpy

# Bibliotecas para algoritmo genético
from deap import base
from deap import creator
from deap import algorithms
from deap import tools
# --------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------------------
# Recebe os dados dos produtos
class Produto:

    def __init__(self, nome, espaco, valor):
        self.nome = nome
        self.espaco = espaco
        self.valor = valor
        

# --------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------------------
# Crianda a lista dos produtos
lista_produtos = []


# Conectando com o banco de dados do mysql
conexao = connect(host='localhost', database='produtos', user='root', password='nosreviejjj7')
cursor = conexao.cursor()
cursor.execute('select nome, espaco, valor, quantidade from produtos')

# preenchendo a lista
for produto in cursor:
    # print(produto[3])
    for i in range(produto[3]):
        lista_produtos.append(Produto(produto[0], produto[1], produto[2]))

cursor.close()
conexao.close()

# Caso não use o banco de dados
"""p1 = Produto("Geladeira Dako", 0.751, 999.90)
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

lista_produtos = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14]"""


# --------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------------------
# Receberão os dados dos produtos
nomes = []
espacos = []
valores = []

for produto in lista_produtos:
    nomes.append(produto.nome)
    espacos.append(produto.espaco)
    valores.append(produto.valor)
    
    
# --------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------------------
# Espaço máximo ocupado no caminhão
limite = 10


# --------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------------------
# Usando as bibliotecas deap

# Função para fazer a inicialização dos recursos da biblioteca
toolbox = base.Toolbox()

# Criando a função de avalição
# Queremos o máximo do valor
# Fitness = avaliação
# weights = parâmetros / pesos
# weights=(1.0, ): valor próximo de 1 é melhor. Próximo de 0 é pior
creator.create("FitnessMax", base.Fitness, weights=(1.0, ))

# Criando o indivíduo
# list: onde ficarão os cromossomos
creator.create("Individual", list, fitness=creator.FitnessMax)

# Fazendo o registro
# Vai preenchero list com os cromossomos
# random.randint, 0, 1: gerar ou zerou ou um, aleatoriamente
# Atributo booleano
toolbox.register("attr_bool", random.randint, 0, 1)

# Aqui vamos passar os indivíduos
# n: tamanho do cromossomo
toolbox.register("individual", tools.initRepeat, creator.Individual,
                 toolbox.attr_bool, n=len(espacos))

# Criação da população
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Função de avaliação

def avaliacao(individual):
    # se quiser definir um valor padrão para a semente do random
    random.seed(1)
    
    nota = 0
    soma_espacos = 0
    for i in range(len(individual)):
        if individual[i] == 1:
            nota += valores[i]
            soma_espacos += espacos[i]
            
    if soma_espacos > limite:
        nota = 1
    # essa "," é por casua da "," do weights=(1.0, )
    # o resultado precisa estar entre 0 e 1, por isso dividir por 1000
    return nota / 100000,

toolbox.register("evaluate", avaliacao)

# crossover
# cxOnePoint: cortar por um ponto apenás no crossover
toolbox.register("mate", tools.cxOnePoint)

# mutação
# flipar o bit com a probabilidade dada
toolbox.register("mutate", tools.mutFlipBit, indpb = 0.01)

# selecionar o pai com a "roleta"
toolbox.register("select",tools.selRoulette)
# --------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    
    # criar uma população
    populacao = toolbox.population(n = 20)
    
    # sempre fará o crossover 100%
    probabilidade_crossover = 1.0
    
    probabilidade_mutacao = 0.01
    
    numero_geracoes = 100
    
    # pegando os valores dos indivíduos
    estatisticas = tools.Statistics(key=lambda individuo: individuo.fitness.values)
    # numpy.max retorna o valor máximo de uma lista
    estatisticas.register("max", numpy.max)
    # valor mínimo
    estatisticas.register("min", numpy.min)
    # valor médio
    estatisticas.register("med", numpy.mean)
    # desvio padrão
    estatisticas.register("std", numpy.std)
    
    # eaSimple é um algoritmo genético
    populacao, info = algorithms.eaSimple(populacao, toolbox,
                                          probabilidade_crossover,
                                          probabilidade_mutacao,
                                          numero_geracoes,
                                          estatisticas)
    
    # pegando o melhor indivíduo
    melhores = tools.selBest(populacao, 1)
    for individuo in melhores:
        print(individuo)
        print(individuo.fitness)
        #print(individuo[0])
        soma = 0
        for i in range(len(lista_produtos)):
            if individuo[i] == 1:
                soma += valores[i]
                print(f"Nome: {lista_produtos[i].nome} R$ {lista_produtos[i].valor}")
        print(f"Melhor solução: {soma}")
        
    # mostrando num gráfico
    valores_grafico = info.select("max")
    plt.plot(valores_grafico)
    plt.title("Acompanhamento dos valores")
    plt.show()