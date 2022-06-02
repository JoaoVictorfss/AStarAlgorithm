class Border :
  def __init__(self) : 
      self.__nos = []
      self.__explorados = []
      self.qtd = 0
  
  def adicionar_no(self, no):
     no_com_prioridade = (no.f, no)
     if no_com_prioridade not in self.__explorados:
        self.qtd = self.qtd + 1
        self.__nos.append(no_com_prioridade)
        self.__explorados.append(no_com_prioridade)
        self.__nos.sort()
  
  def obter_primeiro_no (self):
      primeiro_no = self.__nos.pop(0)[1]
      return primeiro_no
  
  def tem_no_resultado(self, matriz):
      contem_no = False
      for no in self.__nos:
          if(no.compara_matrizes(matriz)):
              contem_no = True
              break
      return contem_no
 
  def obter_no_resultado(self, matriz):
      result = None
      for no in self.__nos:
          if(no.compara_matrizes(matriz)):
              result = no
              break
      return result
          
  def total_de_nos(self):
     return len(self.__nos)
