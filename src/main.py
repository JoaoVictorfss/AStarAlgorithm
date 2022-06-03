from models.Node import Node
from models.Border import Border
from utils.Matriz import Matriz

def resultado(borda, matriz_obj):
  result = None
  while(result is None and borda.qtd < 181440):
    print(f"Quantidade de nós expandidos: {borda.qtd}")
    if(borda.tem_no_resultado(matriz_obj)):
      result = borda.obter_no_resultado(matriz_obj)
    else:
      primeiro_no = borda.obter_primeiro_no()
      primeiro_no.expandir(borda)
    
  print("\n")
  if(result is None):
    print("sem resultado")
    return
  else:
    result.mostrar_resultado()
  
  print(f"Quantidade de nós criados: {borda.qtd - 1}")

# Matrizes objetivos do programa
matriz_obj_1 = [[1,2,3],[4,5,6],[7,8,0]]
matriz_obj_2 = [[0,1,2],[3,4,5],[6,7,8]]

# pega a heuritica
print("\nDigite qual a heuristica para ser usada no jogo: ")
print("Distancia Euclidiana. (Digite 1)\n")
print("Distancia de Manhattan. (Digite 2)")
num_h = input()

# pega a matriz objetivo
print("\nDigite qual o resultado do jogo desejado: ")
print("\nPrimeiro resultado:(Digite 1)")
for i in matriz_obj_1:
  print(i)

print("\nSegundo resultado:(Digite 2)")
for i in matriz_obj_2:
  print(i)

matriz_escolha = int(input().strip())

# pega a matriz inicial
print("\nDigite a sequencia de números do jogo: ")
matriz_inicial = Matriz.crie_matriz(3)

pos_branco = Matriz.acha_branco(matriz_inicial)

# cria a borda e o nó inicial
borda = Border(num_h)
no_inicial = Node(matriz_inicial, pos_branco[0], pos_branco[1])
borda.adicionar_no(no_inicial)

print("\nIsso pode demorar um pouquinho, enquanto isso, recomendamos buscar um café!!\n")
if(matriz_escolha == 1):
  resultado(borda, matriz_obj_1)
elif(matriz_escolha == 2):
  resultado(borda, matriz_obj_2)