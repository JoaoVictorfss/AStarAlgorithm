from utils.Matriz import Matriz
from utils.Heuristics import Heuristics

class Border :
  def __init__(self, h_escolhido) : 
      self.__nos = []
      self.__explorados = []
      self.qtd = 0
      self.h_escolhido = h_escolhido
  
  def adicionar_no(self, no):
    self.__resultado_heuristica(no)
    if no not in self.__explorados:
        self.__nos.append(no)
        self.__nos.sort(key=self.__ordernar)
        self.__explorados.append(no)      
        self.qtd = self.qtd + 1
   
  def obter_primeiro_no (self):
      primeiro_no = self.__nos.pop(0)
      return primeiro_no
  
  def tem_no_resultado(self, matriz):
      contem_no = False
      for no in self.__nos:
          if(Matriz.compara_matrizes(no.matriz, matriz)):
              contem_no = True
              break
      return contem_no
 
  def obter_no_resultado(self, matriz):
      result = None
      for no in self.__nos:
          if(Matriz.compara_matrizes(no.matriz, matriz)):
              result = no
              break
      return result
          
  def total_de_nos(self):
     return len(self.__nos)

  def __resultado_heuristica(self, no):
      if(self.h_escolhido == 1):
          no.h = Heuristics.h1(no.matriz)
      elif(self.h_escolhido == 2):
          no.h = Heuristics.h2(no.matriz)
      no.f = no.g + no.h

  def mostrar_matrizes_na_borda(self):
    for n in self.__nos:
        print(n.matriz)
        
  def __ordernar(self, no):
      return no.f