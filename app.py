from flask import Flask
from flask_cors import CORS
from App.Controllers.livro_controller import livro_bp

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {"msg": "API MVC funcionando 🚀"}

app.register_blueprint(livro_bp)

if __name__ == "__main__":
    app.run(debug=True)