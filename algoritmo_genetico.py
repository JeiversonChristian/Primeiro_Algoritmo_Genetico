# Algoritmo do Caminhão (Aceito sugestões de nomes)


# --------------------------------------------------------------------------------------------------------------------
#Bibliotecas 

# Biblioteca que gera números aleatórios
# não precisa instalar
from random import random
# Biblioteca usada para gerar gráfico
# Para instalar no windons cmd: pip install matplotlib
import matplotlib.pyplot as plt
# Biblioteca que conecta ao banco de dados do mysql
# Para instalar no windons cmd: pip install mysql
from mysql.connector import connect
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
# Cada indivíduo é uma lista de produtos
# A cada indivíduo será associado um cromosso
# Um cromossomo é uma lista de bits que define qual produto levar
# A única coisa que diferencia um indivíduo do outro é o cromossomo
class Individuo:

    def __init__(self, espacos, valores, limite_espacos, geracao=0):

        self.espacos = espacos
        self.valores = valores
        self.limite_espacos = limite_espacos
        self.geracao = geracao
        self.nota_avaliacao = 0
        self.espaco_usado = 0
        self.cromossomo = []

        for i in range(len(lista_produtos)):
            if random() < 0.5:
                self.cromossomo.append(0)
            else:
                self.cromossomo.append(1)

    # Define a nota (somatório dos valores dos produtos) do indivíduo
    # Define o espaço total ocupado pelos produtos do indivíduo
    def avaliacao(self):

        nota = 0
        soma_espacos = 0

        for i in range(len(self.cromossomo)):
            if self.cromossomo[i] == 1:
                nota += self.valores[i]
                soma_espacos += self.espacos[i]
        if soma_espacos > self.limite_espacos:
            nota = 1
        self.nota_avaliacao = nota
        self.espaco_usado = soma_espacos

    # Mistura os genes de dois indivíduos (chamados de pai)
    # E gera filhos com esses genes misturados
    def crossover(self, outro_individuo):

        corte = round(random() * len(self.cromossomo))

        cromossomo_filho1 = outro_individuo.cromossomo[0:corte] + self.cromossomo[corte::]
        cromossomo_filho2 = self.cromossomo[0:corte] + outro_individuo.cromossomo[corte::]

        filho1 = Individuo(self.espacos, self.valores, self.limite_espacos, self.geracao + 1)
        filho2 = Individuo(self.espacos, self.valores, self.limite_espacos, self.geracao + 1)

        filhos = [filho1, filho2]

        filhos[0].cromossomo = cromossomo_filho1
        filhos[1].cromossomo = cromossomo_filho2

        return filhos

    # Muta o indivíduo (o cromossomo dele)
    def mutacao(self, taxa_mutacao):

        for i in range(len(self.cromossomo)):
            if random() < taxa_mutacao:
                if self.cromossomo[i] == 1:
                    self.cromossomo[i] = 0
                else:
                    self.cromossomo[i] = 1

        return self


# --------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------------------
class AlgoritmoGenetico:

    def __init__(self, tamanho_populacao):

        self.tamanho_populacao = tamanho_populacao
        self.populacao = []
        self.geracao = 0
        self.melhor_solucao = 0
        self.lista_solucoes = []

    # gera a 1ª população: lista de indivíduos
    def inicializa_populacao(self, espacos, valores, limite_espacos):

        for i in range(self.tamanho_populacao):
            self.populacao.append(Individuo(espacos, valores, limite_espacos))

        self.melhor_solucao = self.populacao[0]

    # Ordena do indivíduo com a maior nota para o de menor nota
    def ordena_populacao(self):

        # obs.: a chave tem o nome que eu quiser, mas ela é algo que está dentro de "populacao"
        self.populacao = sorted(self.populacao, key=lambda individuo: individuo.nota_avaliacao, reverse=True)

    # Verifica se a nota do indivíduo é a melhor de todas as gerações
    def melhor_individuo(self, individuo):
        if individuo.nota_avaliacao > self.melhor_solucao.nota_avaliacao:
            self.melhor_solucao = individuo
   
    # Soma as notas dos indivíduos para ter um parâmetro que será usado
    # Para selecionar os pais            
    def soma_avaliacoes(self):
        soma = 0
        for individuo in self.populacao:
            soma += individuo.nota_avaliacao
        return soma
    
    # Função do professor - eu fiz a minha própria
    """def seleciona_pai(self, soma_avaliacao):
        pai = -1
        valor_sorteado = random() * soma_avaliacao
        soma = 0
        i = 0
        while i < len(self.populacao) and soma < valor_sorteado:
            soma += self.populacao[i].nota_avaliacao
            pai += 1
            i += 1
        return pai"""

    # Função feita por mim para substituir a função do professor
    # Os indivíduos com maiores notas têm mais chance de serem pais
    def seleciona_pai(self, soma_avaliacao):
        pai = -1
        distancia = soma_avaliacao
        valor_sorteado = random() * soma_avaliacao
        for i in range(len(self.populacao)):
            if abs(valor_sorteado - self.populacao[i].nota_avaliacao) < distancia:
                distancia = abs(valor_sorteado - self.populacao[i].nota_avaliacao)
                pai = i
            elif abs(valor_sorteado - self.populacao[i].nota_avaliacao) == distancia:
                if self.populacao[pai].nota_avaliacao < self.populacao[i].nota_avaliacao:
                    pai = i
        return pai
    
    # Mostra os dados do melhor indivíduo da geração 0
    # Como ela é ordenada, é o primeiro indivíduo
    def visualiza_geracao(self):
        melhor = self.populacao[0]
        print(f"G: {melhor.geracao:3} -> Espaço: {melhor.espaco_usado:.5f} m2 | ", end="")
        print(f"Valor: R$ {melhor.nota_avaliacao:.2f} | Cromossomo: {melhor.cromossomo}")

    # Resolve o problema, associonando cada função do programa
    def resolver(self, taxa_mutacao, numero_geracoes, espacos, valores, limite_espacos):
        self.inicializa_populacao(espacos, valores, limite_espacos)

        # calcula a nota e o espaço de cada indivíduo
        for individuo in self.populacao:
            individuo.avaliacao()

        # Depois de ordenar, o melhor será o primeiro
        self.ordena_populacao()
        self.melhor_solucao = self.populacao[0]
        # Guarda os melhores de cada geração numa lista
        self.lista_solucoes.append(self.melhor_solucao.nota_avaliacao)

        self.visualiza_geracao()

        # pega as somas das notas dos indivíduos de cada geração
        for geracao in range(numero_geracoes):
            soma_avaliacao = self.soma_avaliacoes()
            # Cada geração será substituída por uma nova
            nova_populacao = []

            # Dois pais geram dois filhos
            # Então só é preciso fazer metade das vezes
            for individuos_gerados in range(0, self.tamanho_populacao, 2):
                pai1 = self.seleciona_pai(soma_avaliacao)
                pai2 = self.seleciona_pai(soma_avaliacao)
    
                filhos = self.populacao[pai1].crossover(self.populacao[pai2])
    
                nova_populacao.append(filhos[0].mutacao(taxa_mutacao))
                nova_populacao.append(filhos[1].mutacao(taxa_mutacao))
    
            # A população atual é substituída
            self.populacao = list(nova_populacao)
    
            for individuo in self.populacao:
                individuo.avaliacao()
    
            self.ordena_populacao()
    
            self.visualiza_geracao()
    
            melhor = self.populacao[0]
            self.lista_solucoes.append(melhor.nota_avaliacao)
            # É preciso verifar se o melhor da geração é o melhor de todos
            self.melhor_individuo(melhor)

        # Mostra o resultado final
        print("\nMelhor solução:")
        print(f"Geração: {self.melhor_solucao.geracao} ")
        mensagem = "Espaço / Valor:"
        print(f"{mensagem.ljust(22)} | {self.melhor_solucao.espaco_usado:.5f} m² | ", end="")
        print(f"R$ {self.melhor_solucao.nota_avaliacao:.2f}")
        mensagem = "Cromossomo:"
        print(f"{mensagem.ljust(22)} | {self.melhor_solucao.cromossomo}")
        print("--------------------------------------------------------------------")

        return self.melhor_solucao.cromossomo
    

# --------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    
    lista_produtos = []
    
    # --------------------------------------------------------------------------------------------
    # Conectando com o banco de dados do mysql
    conexao = connect(host='localhost', database='produtos', user='root', password='nosreviejjj7')
    cursor = conexao.cursor()
    cursor.execute('select nome, espaco, valor, quantidade from produtos')
    for produto in cursor:
        # print(produto[3])
        for i in range(produto[3]):
            lista_produtos.append(Produto(produto[0], produto[1], produto[2]))
    
    cursor.close()
    conexao.close()
    # --------------------------------------------------------------------------------------------
    
    # --------------------------------------------------------------------------------------------
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
    # --------------------------------------------------------------------------------------------

    # --------------------------------------------------------------------------------------------
    # Receberão os dados dos produtos
    nomes = []
    espacos = []
    valores = []

    for produto in lista_produtos:
        nomes.append(produto.nome)
        espacos.append(produto.espaco)
        valores.append(produto.valor)
    # --------------------------------------------------------------------------------------------

    # --------------------------------------------------------------------------------------------
    # Parâmetros para o problema
    limite_espacos = 10
    tamanho_populacao = 20
    taxa_mutacao = 0.01
    numero_geracoes = 100
    # --------------------------------------------------------------------------------------------
    
    # --------------------------------------------------------------------------------------------
    # Inicializando o algoritmo    
    ag = AlgoritmoGenetico(tamanho_populacao)
    # --------------------------------------------------------------------------------------------
    
    #--------------------------------------------------------------------------------------------
    # Pegando o resultado do problema
    resultado = ag.resolver(taxa_mutacao, numero_geracoes, espacos, valores, limite_espacos)
    # --------------------------------------------------------------------------------------------
    
    # --------------------------------------------------------------------------------------------
    # Imprimindo a lista de ítens que serão levados no caminhão
    for i in range(len(lista_produtos)):
        if resultado[i] == 1:
            print(f"{lista_produtos[i].nome.ljust(22)} | ", end="")
            print(f"{lista_produtos[i].espaco:.5f} m² | ", end="")
            print(f"R$ {lista_produtos[i].valor:.2f}")
    # --------------------------------------------------------------------------------------------
    
    # --------------------------------------------------------------------------------------------
    # Mostrando o melhor de cada geração
    
    # Sem gráfico        
    """print()
    for valor in ag.lista_solucoes:
        print(valor)"""
    # Com gráfico    
    plt.plot(ag.lista_solucoes)
    plt.title("Acompanhemento dos Valores")
    plt.show()
    # --------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------------------
