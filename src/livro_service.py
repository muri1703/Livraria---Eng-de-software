def filtrar_livros(livros, genero=None, preco_max=None):
    resultado = []

    for livro in livros:
        if genero is not None and livro.genero != genero:
            continue
        if preco_max is not None and livro.preco > preco_max:
            continue
        resultado.append(livro)

    return resultado
