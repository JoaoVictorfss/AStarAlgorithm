class Node:
    def __init__(self, matriz, xb, yb):
        self.matriz = matriz
        self.xb = xb
        self.yb = yb
        self.node_pai = None
        self.movimento = []
        self.mov_qtd = 0
        self.g = 0 
        self.h = 0 
        self.f = self.g + self.h 

def crie_matriz(n_linhas, n_colunas):
    matriz = []
    for i in range(n_linhas):
        linha = []
        linha += [input()]
        for i in linha:
            linha = i.split(',')
        matriz += [linha]
    return matriz
    
def __anda_esquerda(matriz_t, pos_1, pos_2):
      temp = matriz_t[pos_1][pos_2]
      matriz_t[pos_1][pos_2] = matriz_t[pos_1][pos_2-1]
      matriz_t[pos_1][pos_2-1] = temp
      return matriz_t

def __anda_direita(matriz_t, pos_1, pos_2):
      temp = matriz_t[pos_1][pos_2]
      matriz_t[pos_1][pos_2] = matriz_t[pos_1][pos_2+1]
      matriz_t[pos_1][pos_2+1] = temp
      return matriz_t

def __anda_cima(matriz_t, pos_1, pos_2):
      temp = matriz_t[pos_1][pos_2]
      matriz_t[pos_1][pos_2] = matriz_t[pos_1-1][pos_2]
      matriz_t[pos_1-1][pos_2] = temp
      return matriz_t

def __anda_baixo(matriz_t, pos_1, pos_2):
      temp = matriz_t[pos_1][pos_2]
      matriz_t[pos_1][pos_2] = matriz_t[pos_1+1][pos_2]
      matriz_t[pos_1+1][pos_2] = temp
      return matriz_t