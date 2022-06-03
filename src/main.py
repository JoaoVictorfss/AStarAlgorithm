from models.Node import Node
from models.Border import Border
from utils.Matriz import Matriz

MAX = 181440

def main():
    matriz_obj_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    matriz_obj_2 = [[0,1,2],[3,4,5],[6,7,8]]
    
    coleta_dados_e_mostra_resultado(matriz_obj_1, matriz_obj_2)
    
def coleta_dados_e_mostra_resultado(matriz_obj_1, matriz_obj_2):
    print("\nDigite qual a heuristica para ser usada no jogo: ")
    print("Distancia Euclidiana. (Digite 1)")
    print("Distancia de Manhattan. (Digite 2)\n")
    num_h = input()

    print("\nDigite qual o resultado do jogo desejado: ")
    print("Primeiro resultado:(Digite 1)")
    Matriz.mostra_matriz(matriz_obj_1)
      
    print("\nSegundo resultado:(Digite 2)")
    Matriz.mostra_matriz(matriz_obj_2)
    print()
    matriz_escolha = int(input().strip())

    print("\nDigite a sequencia de números do jogo: ")
    matriz_inicial = Matriz.crie_matriz(3)
    
    matriz_obj = matriz_obj_1 if matriz_escolha == 1 else matriz_obj_2
    borda = Border(int(num_h.strip()), matriz_obj)
    pos_branco = Matriz.acha_branco(matriz_inicial)
    no_inicial = Node(matriz_inicial, pos_branco[0], pos_branco[1])
    borda.adicionar_no(no_inicial)
    
    print("\nIsso pode demorar um pouquinho. Enquanto isso, recomendamos buscar um café!!\n")
    
    resultado(borda, matriz_obj)
      
def resultado(borda, matriz_obj):
  result = None
  while(result is None and borda.qtd_gerados < MAX):
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
  
  print(f"Quantidade de nós criados: {borda.qtd_gerados}\n")
  print(f"Quantidade de nós explorados: {borda.qtd_explorados}")

main()
