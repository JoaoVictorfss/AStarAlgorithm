import heapq

from utils.Matriz import Matriz
from utils.Heuristics import Heuristics
from utils.Log import Log

class Border :
  def __init__(self, h_escolhido, matriz_obj, nome_arquivo_log):
      self.__matriz_obj = matriz_obj
      self.__h_escolhido = h_escolhido
      self.__nome_arquivo_log = nome_arquivo_log
      self.__nos = []
      self.__explorados = []
      self.qtd_gerados = 0
      self.qtd_explorados = 0
  
  def adicionar_no(self, no):
    self.__resultado_heuristica(no)
    self.qtd_gerados = self.qtd_gerados + 1
    if no not in self.__explorados:
        heapq.heappush(self.__nos, (-no.f, self.qtd_explorados, no))
        self.__explorados.append(no)      
        self.qtd_explorados = self.qtd_explorados + 1
        self.__escrever_logs(no)
        
  def obter_primeiro_no (self):
      return heapq.heappop(self.__nos)[-1]
  
  def tem_no_resultado(self, matriz):
      contem_no = False
      for no in self.__nos:
          if(Matriz.compara_matrizes(no[-1].matriz, matriz)):
              contem_no = True
              break
      return contem_no
 
  def obter_no_resultado(self, matriz):
      result = None
      for no in self.__nos:
          if(Matriz.compara_matrizes(no[-1].matriz, matriz)):
              result = no
              break
      return result[-1]
          
  def total_de_nos(self):
     return len(self.__nos)

  def __resultado_heuristica(self, no):
      if(self.__h_escolhido == 1):
          no.h = Heuristics.h1(no.matriz, self.__matriz_obj)
      elif(self.__h_escolhido == 2):
          no.h = Heuristics.h2(no.matriz, self.__matriz_obj)
    
      no.f = no.g + no.h

  def mostrar_matrizes_na_borda(self):
    for n in self.__nos:
        print(n.matriz)

  def __escrever_logs(self, no):
        Log.escrever_em_log_criado(self.__nome_arquivo_log, "\nNovo nó adicionado:\n")
        Log.escrever_em_log_criado(self.__nome_arquivo_log, f"Matriz: \n{Matriz.to_string(no.matriz)}")
        Log.escrever_em_log_criado(self.__nome_arquivo_log, f"f: {no.f}\n")