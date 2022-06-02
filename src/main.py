from models.Node import Node
from models.Border import Border
from utils.Heuristics import Heuristics

borda = Border()

#print("Digite a sequencia de números do jogo: ")
#mod_inicial = crie_matriz(3,3)
# Matrizes objetivos do programa
matriz_obj_1 = [[1,2,3],[4,5,6],[7,8,0]]
matriz_obj_2 = [[0,1,2],[3,4,5],[6,7,8]]
matriz_teste = [[7,2,4],[5,0,6],[8,3,1]]

teste = Node(matriz_teste, 1, 1)
teste2 = Node(matriz_teste, 1, 1)

borda.adicionar_no(teste)

print(borda.total_de_nos())
primeiro = borda.obter_primeiro_no()
print(borda.total_de_nos())
print(primeiro.matriz)
