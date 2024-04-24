from abc import ABC, abstractmethod
from Categoria import Categoria
from Produto import Produto
from DesktopAndNotebook import Desktop, Notebook

#Criando categorias
portatil = Categoria(1, 'portatil')
MiniTower = Categoria(2, 'MiniTower')
MidTower = Categoria(3, 'MidiTower')
BigTower = Categoria(4, 'BigTower')
#Criando categorias
#- - - - - - - - - - - - - - - - - - - - - - - - - - - 
#Criando Produtos
asusNotebook = Produto("Notebook Asus Vivobook 15", 1.500, "Preto", portatil )
pcGamer = Produto("Pc Gamer de Itati", 8.000, "Preto", BigTower)
#Criando Produtos
#- - - - - - - - - - - - - - - - - - - - - - - - - - - 
#Criando Desktops e Notebooks

asusnotebookcriado = Notebook("Notebook Asus Vivobook 15", 1.500, "Preto", portatil, "25h")
pcGamerCriado = Desktop("Pc Gamer de Itati", 8.000, "Preto", BigTower, "500W")

#Criando Desktops e Notebooks
#- - - - - - - - - - - - - - - - - - - - - - - - - - - 


#Utilizando classes

print(asusnotebookcriado.__getinfos__())
print('-*' * 20)
print(pcGamerCriado.__getinfos__())