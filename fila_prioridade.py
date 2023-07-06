from lista_ligada import LinkedList

class fila_prioridade(LinkedList):
  def __init__(self):
    self.prio_fila = LinkedList()
    self.fila = LinkedList()

def enfila(self,valor):
  if valor >= 60:
    self.prio_fila.inserir_fim(valor)
  else: 
    self.fila.inserir_final(valor)

def desenfila(self,valor):
  if self.prio_fila == None:
    self.fila.remove(0)
  
def search(self,valor):
  self.fila.procura(valor)
  self.prio_fila.procura(valor)
