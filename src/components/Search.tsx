import Fuse from "fuse.js";
import { useState } from "react";

const options = {
  keys: ["content", "decription"],
  includeMatches: true,
  minMatchCharLength: 2,
  threshold: 0.5,
};

function Search({ searchList }: { searchList: any }) {
  const [query, setQuery] = useState("");

  const fuse = new Fuse(searchList, options);

  const allResepi = fuse
    .search(query)
    .map((result) => result.item)
    .slice(0, 10);

  function handleOnSearch(value: string) {
    setQuery(value);
  }

  return (
    <div className="flex flex-col">
      <div className="flex flex-col mt-4 px-8">
        <input
          type="text"
          name="search"
          id="search"
          value={query}
          onChange={(e) => handleOnSearch(e.target.value)}
          placeholder="Cari resepi"
          className="input input-bordered input-primary w-full"
        />

        {query.length > 1 && (
          <p className="mt-2 font-medium">
            {allResepi.length} resepi dijumpai untuk kata kunci carian '{query}'
          </p>
        )}
      </div>

      <div className="mx-10">
        <h1 className="text-xl font-semibold">
          Disclaimer: Site belum siap sepenuhnya
        </h1>
      </div>

      <div className="mt-4 px-10">
        {query.length < 2 ? (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {searchList.map((item: any) => (
              <div className="card card-compact w-96 bg-base-100 shadow-md">
                <figure className="w-auto h-48">
                  <img
                    src={item.thumbnailUrl}
                    alt=""
                    className="object-cover"
                  />
                </figure>
                <div className="card-body">
                  <a href={item.url}>{item.content}</a>
                </div>
              </div>
            ))}
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {allResepi &&
              allResepi.map((resepi: any) => (
                <div className="card card-compact w-96 bg-base-100 shadow-md">
                  <figure className="w-auto h-48">
                    <img
                      src={resepi.thumbnailUrl}
                      alt=""
                      className="object-cover"
                    />
                  </figure>
                  <div className="card-body">
                    <a href={resepi.url}>{resepi.content}</a>
                  </div>
                </div>
              ))}
          </div>
        )}
      </div>

      <div className="mt-2 px-8 text-lg">
        <h3>Jumlah resepi terkini: {searchList.length}</h3>
      </div>
    </div>
  );
}

export default Search;
