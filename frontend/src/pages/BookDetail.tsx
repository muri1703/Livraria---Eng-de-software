import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import { getLivroById } from "../services/api";

type Livro = {
  id: number;
  titulo: string;
  autor: string;
  preco: number;
  genero: string;
  imagem: string;
};

export function BookDetail() {
  const { id } = useParams();
  const [book, setBook] = useState<Livro | null>(null);

  useEffect(() => {
    async function fetchData() {
      const data = await getLivroById(String(id));
      setBook(data);
    }
    fetchData();
  }, [id]);

  if (!book) return <p>Carregando...</p>;

  return (
    <div className="grid grid-cols-2 gap-10">
      <img src={book.imagem} className="w-full rounded-2xl" />

      <div>
        <h1 className="text-3xl font-bold">{book.titulo}</h1>
        <p>{book.autor}</p>
        <p>R$ {book.preco}</p>
        <p>{book.genero}</p>
      </div>
    </div>
  );
}