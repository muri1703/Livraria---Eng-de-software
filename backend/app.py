from flask import Flask
from flask_cors import CORS
from controllers.livro_controller import livro_bp

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "<h1>API da Livraria está rodando 🚀</h1>"

app.register_blueprint(livro_bp)

if __name__ == "__main__":
    app.run(debug=True)