class Movement:
   # função que faz o quadrado branco andar para esquerda
  def anda_esquerda(matriz_t, pos_1, pos_2):
      temp = matriz_t[pos_1][pos_2]
      matriz_t[pos_1][pos_2] = matriz_t[pos_1][pos_2-1]
      matriz_t[pos_1][pos_2-1] = temp
      return matriz_t

  # função que faz o quadrado branco andar para direita
  def anda_direita(matriz_t, pos_1, pos_2):
      temp = matriz_t[pos_1][pos_2]
      matriz_t[pos_1][pos_2] = matriz_t[pos_1][pos_2+1]
      matriz_t[pos_1][pos_2+1] = temp
      return matriz_t

  # função que faz o quadrado branco andar para cima
  def anda_cima(matriz_t, pos_1, pos_2):
      temp = matriz_t[pos_1][pos_2]
      matriz_t[pos_1][pos_2] = matriz_t[pos_1-1][pos_2]
      matriz_t[pos_1-1][pos_2] = temp
      return matriz_t

  # função que faz o quadrado branco andar para baixo
  def anda_baixo(matriz_t, pos_1, pos_2):
      temp = matriz_t[pos_1][pos_2]
      matriz_t[pos_1][pos_2] = matriz_t[pos_1+1][pos_2]
      matriz_t[pos_1+1][pos_2] = temp
      return matriz_t