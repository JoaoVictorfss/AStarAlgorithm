from models.Node import Node
from models.Border import Border
from utils.Matriz import Matriz

def resultado(borda, matriz_obj, no_inicial):
  print("Entrei")
  no_inicial.expandir(borda)#estado inicial da borda
  result = None
  while(result is None and borda.qtd < 181440):        
    if(borda.tem_no_resultado(matriz_obj)):
      result = borda.obter_no_resultado(matriz_obj)
    else:
      primeiro_no = borda.obter_primeiro_no()
      primeiro_no.expandir(borda)

    if(result is None):
      print("sem resultado")
    else:
      result.mostrar_resultado()

# Matrizes objetivos do programa
matriz_obj_1 = [[1,2,3],[4,5,6],[7,8,0]]
matriz_obj_2 = [[0,1,2],[3,4,5],[6,7,8]]

# pega a heuritica
print("\nDigite qual a heuristica para ser usada no jogo: ")
print("Heuristica que conta quantos numeros estão fora do lugar. (Digite 1)\n")
print("Distancia de Manhattan. (Digite 2)\n")
num_h = input()

# pega a matriz objetivo
print("Digite qual o resultado do jogo desejado: ")
print("\nPrimeiro resultado:(Digite 1)")
for i in matriz_obj_1:
  print(i)

print("\nSegundo resultado:(Digite 2)")
for i in matriz_obj_2:
  print(i)

print("\n")
matriz_escolha = input()

# pega a matriz inicial
print("\nDigite a sequencia de números do jogo: ")
matriz_inicial = Matriz.crie_matriz(3)

pos_branco = Matriz.acha_branco(matriz_inicial)

# cria a borda e o nó inicial
borda = Border(num_h)
no_inicial = Node(matriz_inicial, pos_branco[0], pos_branco[1])

if(matriz_escolha == 1):
  resultado(borda, matriz_obj_1, no_inicial)
elif(matriz_escolha == 2):
  resultado(borda, matriz_obj_2, no_inicial)



