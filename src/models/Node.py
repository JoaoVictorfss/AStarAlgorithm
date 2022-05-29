#Classe dos nodes
class Node:
    def __init__(self, matriz, xb, yb):
        self.matriz = matriz
        self.xb = xb
        self.yb = yb
        self.node_pai = Node
        self.movimento = []
        self.mov_qtd = 0
        self.g = 0 # g do pai + 1
        self.h = 0 # custo de sair do nó até o final
        self.f = self.g + self.h # custo, quanto menor, maior a prioridade na borda

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

def anda_esquerda(matriz_t, pos_1, pos_2):
      temp = matriz_t[pos_1][pos_2]
      matriz_t[pos_1][pos_2] = matriz_t[pos_1][pos_2-1]
      matriz_t[pos_1][pos_2-1] = temp
      return matriz_t

  # função que faz o quadrado branco andar para direita
def anda_direita(matriz_t, pos_1, pos_2):
      temp = matriz_t[pos_1][pos_2]
      matriz_t[pos_1][pos_2] = matriz_t[pos_1][pos_2+1]
      matriz_t[pos_1][pos_2+1] = temp
      return matriz_t

  # função que faz o quadrado branco andar para cima
def anda_cima(matriz_t, pos_1, pos_2):
      temp = matriz_t[pos_1][pos_2]
      matriz_t[pos_1][pos_2] = matriz_t[pos_1-1][pos_2]
      matriz_t[pos_1-1][pos_2] = temp
      return matriz_t

  # função que faz o quadrado branco andar para baixo
def anda_baixo(matriz_t, pos_1, pos_2):
      temp = matriz_t[pos_1][pos_2]
      matriz_t[pos_1][pos_2] = matriz_t[pos_1+1][pos_2]
      matriz_t[pos_1+1][pos_2] = temp
      return matriz_t