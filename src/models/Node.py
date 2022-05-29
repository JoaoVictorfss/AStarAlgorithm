#Classe dos nodes
class Node:

    def __init__(self, matriz, xb, yb):
        self.matriz = matriz
        self.xb = xb
        self.yb = yb
        self.node_pai = Node
        self.movimento = []
        self.mov_qtd = 0
        self.g = 0
        self.h = 0
        self.f = self.g + self.h

# funçao que cria a matriz inicial do jogo
def crie_matriz(n_linhas, n_colunas):
    matriz = []
    for i in range(n_linhas):
        linha = []
        linha += [input()]
        for i in linha:
            linha = i.split(',')
        matriz += [linha]
    return matriz
