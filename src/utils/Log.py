from datetime import datetime
from utils.Matriz import Matriz

class Log:
  @staticmethod
  def escrever_novo_log(matriz_obj, matriz_inicial, nome_arquivo):
        horario = datetime.now()
        f = open(f"logs/{nome_arquivo}", "w")
        f.write("Teste iniciado em " + horario.strftime("%d/%m/%Y às %H:%M:%S") + "\n")
        
        f.write(f"Matriz objetivo:\n")
        f.write(Matriz.to_string(matriz_obj))
        f.write("\n")

        f.write(f"Matriz Inicial:\n")
        f.write(Matriz.to_string(matriz_inicial))
        f.write("\n")

        f.close()
        
  @staticmethod
  def escrever_em_log_criado(nome_arquivo, conteudo):
        f = open(f"logs/{nome_arquivo}", "a")
        f.write(conteudo)
        f.close()
