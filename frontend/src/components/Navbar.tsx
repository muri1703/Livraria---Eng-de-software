export function Navbar() {
  return (
    <nav className="bg-zinc-900 border-b border-zinc-800 px-8 py-4 flex justify-between items-center">

      <h1 className="text-orange-500 text-2xl font-bold">
        📚 Livraria
      </h1>

      <div className="flex gap-6 text-white">
        <a href="/" className="hover:text-orange-400 transition">
          Home
        </a>

        <a href="/search" className="hover:text-orange-400 transition">
          Buscar
        </a>
      </div>

    </nav>
  );
}