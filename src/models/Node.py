import numpy as np
from copy import deepcopy

class Node:
    def __init__(self, matriz, xb, yb):
        self.matriz = matriz
        self.xb = xb
        self.yb = yb
        self.node_pai = None
        self.movimento = None
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
    
    def expandir(self, borda):  
        matriz_baixo = self.__anda_baixo()
        matriz_cima = self.__anda_cima()
        matriz_direita = self.__anda_direita()
        matriz_esquerda = self.__anda_esquerda()
        
        #valores de f são para testes, o calculo deve ser feito
        no_baixo = self.__cria_no(matriz_baixo, self.xb + 1, self.yb, "baixo", 1 )
        no_cima = self.__cria_no(matriz_cima, self.xb - 1, self.yb, "cima", 2)
        no_direita = self.__cria_no(matriz_direita, self.xb, self.yb + 1, "direita", 3)
        no_esquerda = self.__cria_no(matriz_esquerda, self.xb, self.yb - 1, "esquerda", 4)
        
        borda.adicionar_no(no_baixo)
        borda.adicionar_no(no_cima)
        borda.adicionar_no(no_direita)
        borda.adicionar_no(no_esquerda)
        
    def compara_matrizes(self, no):
        matriz1 = np.array(self.matriz)
        matriz2 = np.array(no.matriz)
        return (matriz1 == matriz2).all()
    
    def __cria_no(self, matriz, xb, yb, movimento, h):
       novo_no = Node(matriz, xb, yb)
       novo_no.node_pai = self
       novo_no.g = self.g + 1
       novo_no.h = h
       novo_no.f = novo_no.g + novo_no.h
       novo_no.movimento = movimento
       
       return novo_no
       
    def __anda_baixo(self):
        matriz_t = deepcopy(self.matriz)
        temp = deepcopy(matriz_t[self.xb][self.yb])
        matriz_t[self.xb][self.yb] = matriz_t[self.xb+1][self.yb]
        matriz_t[self.xb+1][self.yb] = temp
        return matriz_t
    
    def __anda_cima(self):
        matriz_t = deepcopy(self.matriz)
        temp = deepcopy(matriz_t[self.xb][self.yb])
        matriz_t[self.xb][self.yb] = matriz_t[self.xb-1][self.yb]
        matriz_t[self.xb-1][self.yb] = temp
        return matriz_t
    
    def __anda_direita(self):
        matriz_t = deepcopy(self.matriz)
        temp = deepcopy(matriz_t[self.xb][self.yb])
        matriz_t[self.xb][self.yb] = matriz_t[self.xb][self.yb+1]
        matriz_t[self.xb][self.yb+1] = temp
        return matriz_t
    
    def __anda_esquerda(self):
        matriz_t = deepcopy(self.matriz)
        temp = deepcopy(matriz_t[self.xb][self.yb])
        matriz_t[self.xb][self.yb] = matriz_t[self.xb][self.yb-1]
        matriz_t[self.xb][self.yb-1] = temp
        return matriz_t
