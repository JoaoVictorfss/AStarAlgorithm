class Border :
  def __init__(self) : 
      self.__nos = []
      self.__explorados = []
      self.qtd = 0
  
  def adicionar_no_explorado(self, no):
      novo_no_explorado = (no.f, no)
      self.__explorados.append(novo_no_explorado)
  
  def adicionar_no(self, no):
     no_com_prioridade = (no.f, no)
     if no_com_prioridade not in self.__explorados:
        self.qtd = self.qtd + 1
        self.__nos.append(no_com_prioridade)
        self.__nos.sort()
        self.adicionar_no_explorado(no)
  
  def obter_primeiro_no (self):
      primeiro_no = self.__nos[0][1]
      return primeiro_no
  
  def tem_no_resultado(matrix_obj, self):
      return (matrix_obj in self.__nos)
 
  def obter_no_resultado(self, matrix):
      for no in self.__nos:
          if(matrix == no.matrix):
              return no

