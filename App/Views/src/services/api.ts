// LISTA / BUSCA
export async function getLivros(query?: string) {
  let url = "http://127.0.0.1:5000/livros";

  if (query && query.trim() !== "") {
    url += `?q=${encodeURIComponent(query)}`;
  }

  console.log("URL:", url);

  const res = await fetch(url);
  return res.json();
}

// DETALHE POR ID
export async function getLivroById(id: string) {
  const res = await fetch(`http://127.0.0.1:5000/livros/${id}`);
  return res.json();
}