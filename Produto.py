from abc import ABC, abstractmethod
from Categoria import Categoria

@abstractmethod
class Produto(ABC):
    def __init__(self,modelo, preco, cor, categoria):
        self.modelo = modelo
        self.preco = preco
        self.cor = cor
        self.categoria = categoria
    def __getinfos__(self):
        info_str = ""
        for attr, value in vars(self).items():
            info_str += f"{attr}: {value}\n"
        return info_str
    def cadastrar (self):
        while True:
            perfumaria = input('Cadastrar Produto? S/N').upper()
            if perfumaria == "S":
                print("Produto cadastrado")
                exit()
            elif perfumaria == "N":
                print('Produto não cadastrado')
                exit()
            else:
                print("Insira apenas S ou N")


 

