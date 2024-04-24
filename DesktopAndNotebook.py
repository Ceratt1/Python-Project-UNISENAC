from abc import ABC, abstractmethod
from Categoria import Categoria
from Produto import Produto

class Desktop(Produto):
    def __init__(self, modelo, preco, cor, categoria, potencia_da_fonte):
        super().__init__(modelo, preco, cor, categoria)
        self._potenciaDaFonte = potencia_da_fonte
    def __setPotencia__(self,nova_potencia):
        self._potenciaDaFonte = nova_potencia
    
class Notebook(Produto):
    def __init__(self, modelo, preco, cor, categoria, tempoBateria):
        super().__init__(modelo, preco, cor, categoria)
        self.__tempoBateria = tempoBateria

    def __setBateria__(self,novo_tempo_bateria):
        self.__tempoBateria = novo_tempo_bateria
    

