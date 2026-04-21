import { useParams } from "react-router-dom";

export function Book() {
  const { id } = useParams();

  return (
    <div className="bg-white p-10 rounded-2xl shadow max-w-3xl mx-auto">

      <img
        src={`https://picsum.photos/300/400?random=${id}`}
        className="w-60 rounded mb-6"
      />

      <h1 className="text-3xl font-bold">{id}</h1>

      <p className="text-gray-500 mt-2">
        Autor fictício
      </p>

      <p className="mt-4 text-gray-700">
        Descrição do livro aqui...
      </p>

      <button className="mt-6 bg-orange-500 text-white px-6 py-2 rounded">
        Reservar
      </button>

    </div>
  );
}