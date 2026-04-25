import unittest
from livro import Livro
from livro_service import filtrar_livros


class TestLivroService(unittest.TestCase):

    def setUp(self):
        self.livros = [
            Livro("Livro A", "Autor 1", 50.0, "Fantasia"),
            Livro("Livro B", "Autor 2", 30.0, "Romance"),
            Livro("Livro C", "Autor 3", 40.0, "Fantasia"),
        ]
        
    def test_lista_vazia(self):
        resultado = filtrar_livros([])
        self.assertEqual(len(resultado), 0)
        
    def test_sem_filtro(self):
        resultado = filtrar_livros(self.livros)
        self.assertEqual(len(resultado), 3)

    def test_filtrar_por_genero(self):
        resultado = filtrar_livros(self.livros, genero="Fantasia")
        self.assertEqual(len(resultado), 2)

    def test_filtrar_por_preco(self):
        resultado = filtrar_livros(self.livros, preco_max=40.0)
        self.assertEqual(len(resultado), 2)

    def test_filtrar_genero_e_preco(self):
        resultado = filtrar_livros(self.livros, genero="Fantasia", preco_max=45.0)
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0].titulo, "Livro C")
        
if __name__ == "__main__":
    unittest.main()
