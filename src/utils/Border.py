import heapq as hq

class Border :
  def __init__(self) : 
      self.borda = []
      self.explorados = []

  def obter_borda(self):
     return hq.heapify(self.borda)