import numpy as np

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

    def __eq__(self, outro_no):
        matriz1 = np.array(self.matriz)
        matriz2 = np.array(outro_no.matriz)
        
        return (self.xb == outro_no.xb and 
                  self.yb == outro_no.yb and 
                  self.f == outro_no.f and 
                  self.h == outro_no.h and 
                  self.g == outro_no.g and
                  self.mov_qtd == outro_no.mov_qtd and 
                 (matriz1 == matriz2).all() #comparação de matrizes
        )
        
    def crie_matriz(n_linhas, n_colunas):
        matriz = []
        for i in range(n_linhas):
            linha = []
            linha += [input()]
            for i in linha:
                linha = i.split(',')
            matriz += [linha]
        return matriz

    def compara_matrizes(self, no):
        matriz1 = np.array(self.matriz)
        matriz2 = np.array(no.matriz)
        return (matriz1 == matriz2).all()
        
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
        