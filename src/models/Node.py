from copy import deepcopy
from utils.Matriz import Matriz

from utils.Log import Log

class Node:
    def __init__(self, matriz, xb, yb):
        self.matriz = matriz
        self.xb = xb
        self.yb = yb
        self.node_pai = None
        self.movimento = None
        self.g = 0 
        self.h = 0 
        self.f = self.g + self.h 

    def __eq__(self, outro_no):
        if(outro_no is None):
          return False
        return Matriz.compara_matrizes(self.matriz, outro_no.matriz)

    def __ne__(self, outro_no):
        return not Matriz.compara_matrizes(self.matriz, outro_no.matriz)

    def __lt__(self, outro_no):
        return self.f < outro_no.f

    def __gt__(self, outro_no):
        return self.f > outro_no.f

    def __le__(self, outro_no):
        return self.f <= outro_no.f

    def __ge__(self, outro_no):
        return self.f >= outro_no.f

    def mostrar_resultado(self, nome_arquivo_log):
        no = self
        passo = 1
        nos_com_resultado = []           
        
        print("\nPassos para chegar no resultado:")   
        while(no is not None and no.node_pai is not None):
            nos_com_resultado.append(no)
            no = no.node_pai
        if(len(nos_com_resultado) == 0):
          print("  Não faça nada")
          Log.escrever_em_log_criado(nome_arquivo_log, "\nMovimentos: Não faça nada\n")
        else:
          nos_em_ordem = nos_com_resultado[::-1]
          for no in nos_em_ordem:
              print(f"{passo} - Mova o branco para {no.movimento}\n")
              print(f"{Matriz.to_string(no.matriz)}")
              Log.escrever_em_log_criado(nome_arquivo_log, f"{passo} - Mova o branco para {no.movimento}\n")
              Log.escrever_em_log_criado(nome_arquivo_log, Matriz.to_string(no.matriz) + "\n")
              passo += 1         
          
    def expandir(self, borda):  
        #Expande para baixo
        if(self.xb + 1 <= 2):
          matriz_baixo = self.__anda_baixo()
          no_baixo = self.__cria_no(matriz_baixo, self.xb + 1, self.yb, "baixo")
          borda.adicionar_no(no_baixo)
        
        #Expande para cima
        if(self.xb - 1 >= 0):
          matriz_cima = self.__anda_cima()
          no_cima = self.__cria_no(matriz_cima, self.xb - 1, self.yb, "cima")
          borda.adicionar_no(no_cima)
        
        #Expande para direita
        if(self.yb + 1 <= 2):
          matriz_direita = self.__anda_direita()
          no_direita = self.__cria_no(matriz_direita, self.xb, self.yb + 1, "direita")
          borda.adicionar_no(no_direita)
          
        #Expande para esquerda
        if(self.yb - 1 >= 0) :
          matriz_esquerda = self.__anda_esquerda()
          no_esquerda = self.__cria_no(matriz_esquerda, self.xb, self.yb - 1, "esquerda")
          borda.adicionar_no(no_esquerda)  
          
    def __cria_no(self, matriz, xb, yb, movimento):
       novo_no = Node(matriz, xb, yb)
       novo_no.node_pai = self
       novo_no.g = self.g + 1
       novo_no.movimento = movimento    
       return novo_no
       
    def __anda_baixo(self):
        matriz_t = deepcopy(self.matriz)
        temp = deepcopy(matriz_t[self.xb][self.yb])
        matriz_t[self.xb][self.yb] = matriz_t[self.xb+1][self.yb]
        matriz_t[self.xb+1][self.yb] = temp
        return matriz_t
    
    def __anda_cima(self):
        matriz_t = deepcopy(self.matriz)
        temp = deepcopy(matriz_t[self.xb][self.yb])
        matriz_t[self.xb][self.yb] = matriz_t[self.xb-1][self.yb]
        matriz_t[self.xb-1][self.yb] = temp
        return matriz_t
    
    def __anda_direita(self):
        matriz_t = deepcopy(self.matriz)
        temp = deepcopy(matriz_t[self.xb][self.yb])
        matriz_t[self.xb][self.yb] = matriz_t[self.xb][self.yb+1]
        matriz_t[self.xb][self.yb+1] = temp
        return matriz_t
    
    def __anda_esquerda(self):
        matriz_t = deepcopy(self.matriz)
        temp = deepcopy(matriz_t[self.xb][self.yb])
        matriz_t[self.xb][self.yb] = matriz_t[self.xb][self.yb-1]
        matriz_t[self.xb][self.yb-1] = temp
        return matriz_t
