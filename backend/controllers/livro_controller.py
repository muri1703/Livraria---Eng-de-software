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

# 🔍 BUSCA COM FILTRO
@livro_bp.route("/livros", methods=["GET"])
def get_livros():
    query = request.args.get("q", "").lower()

    if query:
        resultado = [
            l for l in livros
            if query in l["titulo"].lower()
            or query in l["autor"].lower()
            or query in l["genero"].lower()
        ]
    else:
        resultado = livros

    return jsonify(resultado)


# 📚 BUSCAR POR ID
@livro_bp.route("/livros/<int:id>", methods=["GET"])
def get_livro_por_id(id):
    livro = next((l for l in livros if l["id"] == id), None)

    if livro:
        return jsonify(livro)

    return jsonify({"erro": "Livro não encontrado"}), 404