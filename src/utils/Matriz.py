import numpy as np

class Matriz:
    @staticmethod
    def crie_matriz(n_linhas, n_colunas):
        matriz = []
        for i in range(n_linhas):
            linha = []
            linha += [input()]
            for i in linha:
                linha = i.split(',')
            matriz += [linha]
        return matriz

    @staticmethod
    def compara_matrizes(matriz1, matriz2):
        matriz1_np = np.array(matriz1)
        matriz2_np = np.array(matriz2)
        return (matriz1_np == matriz2_np).all()
