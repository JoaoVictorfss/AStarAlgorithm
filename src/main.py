from models.Node import Node
from utils.Border import Border
from utils.Heuristics import Heuristics

#print("Digite a sequencia de números do jogo: ")
#mod_inicial = crie_matriz(3,3)
# Matrizes objetivos do programa
matriz_obj_1 = [[1,2,3],[4,5,6],[7,8,0]]
matriz_obj_2 = [[0,1,2],[3,4,5],[6,7,8]]
matriz_teste = [[7,2,4],[5,0,6],[8,3,1]]

teste = Node(matriz_teste, 1, 1)

print(teste.matriz)