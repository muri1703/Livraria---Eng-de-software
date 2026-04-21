import { Link } from "react-router-dom";

type Livro = {
  id: number;
  titulo: string;
  autor: string;
  preco: number;
  genero: string;
  imagem: string;
};


export function BookCard({ book }: { book: Livro }) {
  return (
    <Link to={`/book/${book.id}`}>
      <div className="bg-gray-800 rounded-2xl overflow-hidden shadow-lg hover:scale-105 transition cursor-pointer">

        <img
          src={book.imagem}
          alt={book.titulo}
          className="w-full h-64 object-cover"
        />

        <div className="p-4">
          <h3 className="font-bold text-lg text-white">
            {book.titulo}
          </h3>

          <p className="text-gray-400 text-sm">
            {book.autor}
          </p>

          <p className="text-orange-400 font-bold mt-2">
            R$ {book.preco}
          </p>
        </div>

      </div>
    </Link>
  );
}