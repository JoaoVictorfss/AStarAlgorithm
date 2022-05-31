class Border :
  def __init__(self) : 
      self.__nos = []
      self.__explorados = []
  
  def adicionar_no_explorado(self, no):
      novo_no_explorado = (no.f, no)
      self.__explorados.append(novo_no_explorado)
  
  def adicionar_no(self, no):
     no_com_prioridade = (no.f, no)
     if no_com_prioridade not in self.__explorados:
        self.__nos.append(no_com_prioridade)
        self.__nos.sort()
  
  def size (self):
      return len(self.__nos)
  
  def first (self):
      return self.__nos[0][1]
    