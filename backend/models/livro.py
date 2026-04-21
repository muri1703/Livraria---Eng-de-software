class Livro:
    def __init__(self, titulo, autor, preco, genero, imagem):
        self.id = titulo.lower().replace(" ", "-")
        self.titulo = titulo
        self.autor = autor
        self.preco = preco
        self.genero = genero
        self.imagem = imagem