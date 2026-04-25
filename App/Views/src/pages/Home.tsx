import { useEffect, useState } from "react";
import { getLivros } from "../services/api";
import { BookCard } from "../components/BookCard";

type Livro = {
  id: number;
  titulo: string;
  autor: string;
  preco: number;
  genero: string;
  imagem: string;
};

export function Home() {
  const [livros, setLivros] = useState<Livro[]>([]);

  useEffect(() => {
    async function fetchData() {
      const data = await getLivros("");
      setLivros(data);
    }

    fetchData();
  }, []);

  return (
    <div className="space-y-10">

      {/* HERO */}
      <div className="bg-gradient-to-r from-orange-500 to-red-500 p-12 rounded-3xl text-white shadow-lg">
        <h1 className="text-5xl font-bold mb-4">
          Descubra seu próximo livro 📚
        </h1>
        <p className="text-lg text-orange-100">
          Explore nossa coleção e encontre histórias incríveis
        </p>
      </div>

      {/* DESTAQUES */}
      <div>
        <h2 className="text-2xl font-bold mb-6 text-white">
          Destaques da Semana
        </h2>

        <div className="grid grid-cols-4 gap-6">
          {livros.map((l) => (
            <BookCard key={l.id} book={l} />
          ))}
        </div>
      </div>

    </div>
  );
}