import numpy as np

class Matriz:
    @staticmethod
    def crie_matriz(n_linhas):
        matriz = []
        for i in range(n_linhas):
            linha = []
            linha += [input()]
            for i in linha:
                linha = i.split(',')
                linha = [int(l.strip()) for l in linha]
            matriz += [linha]
        return matriz

    @staticmethod
    def compara_matrizes(matriz1, matriz2):
        matriz1_np = np.array(matriz1)
        matriz2_np = np.array(matriz2)
        return (matriz1_np == matriz2_np).all()
    
    @staticmethod
    def acha_branco(matriz_inicial):
        x = 0
        xb = 0
        yb = 0
        for i in matriz_inicial:
            y = 0
            for j in i:
                if(j == 0 ):
                    xb = x
                    yb = y
                    break
                y += 1                
            x += 1
        return [xb,yb]