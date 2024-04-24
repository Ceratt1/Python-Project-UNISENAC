class Categoria:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    def __str__(self) -> str:
        return f'id: {self.id} | Nome_Categoria: {self.nome}'



