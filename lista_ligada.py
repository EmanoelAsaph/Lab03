from estrutura_elementar import estrutura_elementar


class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def set_proximo(self, no):
        self.proximo = no

    def get_proximo(self):
        return self.proximo


class LinkedList(estrutura_elementar):
    def __init__(self):
        self.inicio = None

    def inserir_inicio(self, valor):
        if self.inicio is None:
            self.inicio = No(valor)
        else:
            novoNo = No(valor)
            novoNo.set_proximo(self.inicio)
            self.inicio = novoNo

    def inserir_fim(self, valor):
        if self.inicio is None:
            self.inicio = No(valor)
        else:
            novoNo = No(valor)
            aux = self.inicio
            while aux.get_proximo() is not None:
                aux = aux.get_proximo()
            aux.set_proximo(novoNo)

    def esta_vazio(self) -> bool:
        if self.inicio is None:
            return True
        else:
            return False
     
    def remove(self, item):
        
        pass

    def tamanho(self) -> int:
        if self.inicio is None:
            return 0
        else:
            contador = 1
            aux = self.inicio
            while aux.get_proximo() is not None:
                aux = aux.get_proximo()
                contador += 1
            return contador       

    def limpa(self):
        self.inicio = None
        pass
       
    def procura(self, item) -> bool:
    
            
        return False

    def indice_de(self, item): 
        if self.inicio is None:
            return-1
        

            
    pass

                
    def recupera_indice(self, index):
        return 1
