from models.Node import Node
from models.Border import Border
from utils.Matriz import Matriz
from utils.Log import Log
from datetime import datetime

MAX = 181440

def main():
    horario = datetime.now()
    nome_arquivo_log = "teste_" + horario.strftime("%d_%m_%Y:%H:%M:%S") + ".txt"     
    matriz_obj_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    matriz_obj_2 = [[0,1,2],[3,4,5],[6,7,8]]
    
    coleta_dados_e_mostra_resultado(matriz_obj_1, matriz_obj_2, nome_arquivo_log)
    
def coleta_dados_e_mostra_resultado(matriz_obj_1, matriz_obj_2, nome_arquivo_log):
    print("\nDigite qual a heuristica para ser usada no jogo: ")
    print("  Distancia Euclidiana. (Digite 1)")
    print("  Distancia de Manhattan. (Digite 2)\n")
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
    borda = Border(int(num_h.strip()), matriz_obj, nome_arquivo_log)
    pos_branco = Matriz.acha_branco(matriz_inicial)
    
    Log.escrever_novo_log(matriz_obj, matriz_inicial, nome_arquivo_log)
    Log.escrever_em_log_criado(nome_arquivo_log, "Estados:\n")
    
    no_inicial = Node(matriz_inicial, pos_branco[0], pos_branco[1])
    borda.adicionar_no(no_inicial)  
     
    print("\nIsso pode demorar um pouquinho. Enquanto isso, recomendamos buscar um café!!")
    
    resultado(borda, matriz_obj, nome_arquivo_log)
      

def resultado(borda, matriz_obj, nome_arquivo_log):
  result = None
  while(result is None and borda.qtd_gerados < MAX):
    if(borda.tem_no_resultado(matriz_obj)):
      result = borda.obter_no_resultado(matriz_obj)
    else:
      primeiro_no = borda.obter_primeiro_no()
      primeiro_no.expandir(borda)
    
  print("\n")
  if(result is None):
    Log.escrever_em_log_criado(nome_arquivo_log, "\nNenhum resultado encontrado\n")
    print("sem resultado")
  else:
      Log.escrever_em_log_criado(nome_arquivo_log, "\nResultado encontrado: \n")
      result.mostrar_resultado(nome_arquivo_log)
      
  horario = datetime.now()
  Log.escrever_em_log_criado(nome_arquivo_log, f"\nQuantidade de nós criados: {borda.qtd_gerados}\n")
  Log.escrever_em_log_criado(nome_arquivo_log, f"Quantidade de nós explorados: {borda.qtd_explorados}\n")
  Log.escrever_em_log_criado(
      nome_arquivo_log, f"Quantidade de nós na borda: {borda.total_de_nos()}\n")
  Log.escrever_em_log_criado(nome_arquivo_log, "\nTeste finalizado em " + horario.strftime("%d/%m/%Y às %H:%M:%S") + "\n")

  print(f"\nQuantidade de nós criados: {borda.qtd_gerados}")
  print(f"Quantidade de nós explorados: {borda.qtd_explorados}")

main()
