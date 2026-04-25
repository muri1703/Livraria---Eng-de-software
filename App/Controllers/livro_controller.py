from flask import Blueprint, request, jsonify

livro_bp = Blueprint('livro', __name__)

# Banco fake
livros = [
    {
        "id": 1,
        "titulo": "Harry Potter",
        "autor": "J.K Rowling",
        "preco": 50,
        "genero": "Fantasia",
        "imagem": "https://m.media-amazon.com/images/I/81iqZ2HHD-L.jpg"
    },
    {
        "id": 2,
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis",
        "preco": 30,
        "genero": "Clássico",
        "imagem": "https://images.tcdn.com.br/img/img_prod/1271663/dom_casmurro_edicao_de_luxo_almofadada_89_1_038fb70c564eb50f71ea49f6027e827a.jpg"
    },
    {
        "id": 3,
        "titulo": "O Hobbit",
        "autor": "Tolkien",
        "preco": 45,
        "genero": "Fantasia",
        "imagem": "https://m.media-amazon.com/images/I/91b0C2YNSrL.jpg"
    }
]

# 🔍 Função de filtro (fica no controller no MVC simples)
def filtrar_livros(lista, query=None, preco_max=None):
    resultado = []

    for l in lista:
        if query:
            if (
                query not in l["titulo"].lower()
                and query not in l["autor"].lower()
                and query not in l["genero"].lower()
            ):
                continue

        if preco_max is not None:
            if l["preco"] > preco_max:
                continue

        resultado.append(l)

    return resultado


# 🔍 BUSCA
@livro_bp.route("/livros", methods=["GET"])
def get_livros():
    query = request.args.get("q", "").lower()
    preco_max = request.args.get("preco_max", type=float)

    resultado = filtrar_livros(livros, query, preco_max)

    return jsonify(resultado)


# 📚 DETALHE
@livro_bp.route("/livros/<int:id>", methods=["GET"])
def get_livro_por_id(id):
    livro = next((l for l in livros if l["id"] == id), None)

    if livro:
        return jsonify(livro)

    return jsonify({"erro": "Livro não encontrado"}), 404