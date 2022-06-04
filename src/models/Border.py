from queue import PriorityQueue

from utils.Matriz import Matriz
from utils.Heuristics import Heuristics
from utils.Log import Log

H1 = 1
H2 = 2

class Border :
  def __init__(self, h_escolhido, matriz_obj):
      self.__matriz_obj = matriz_obj
      self.__h_escolhido = h_escolhido
      self.__nos = PriorityQueue()
      self.__qtd_nos = 0
      self.__explorados = []
      self.qtd_gerados = 0
      self.qtd_explorados = 0
  
  def adicionar_no(self, no):
    self.__resultado_heuristica(no)
    self.qtd_gerados = self.qtd_gerados + 1
    if no not in self.__explorados:
        self.__nos.put((no.f, no))
        self.__explorados.append(no)      
        self.qtd_explorados = self.qtd_explorados + 1
        self.__qtd_nos += 1
        
  def obter_primeiro_no (self):
        self.__qtd_nos -= 1
        primeiro_no = self.__nos.get()[1]
        return primeiro_no
          
  def total_de_nos(self):
     return self.__qtd_nos

  def __resultado_heuristica(self, no):
      if(self.__h_escolhido == H1):
          no.h = Heuristics.h1(no.matriz, self.__matriz_obj)
      elif(self.__h_escolhido == H2):
          no.h = Heuristics.h2(no.matriz, self.__matriz_obj)
      no.f = no.g + no.h

  def mostrar_matrizes_na_borda(self):
    for n in self.__nos:
        print(n.matriz)