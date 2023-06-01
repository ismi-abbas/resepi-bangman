import Fuse from "fuse.js";
import { useState } from "react";
import Card from "./Card";

const options = {
  keys: ["content"],
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
      {/* Search Bar */}
      <div className="flex flex-col mt-4 items-center px-14 md:px-0">
        <input
          type="text"
          name="search"
          id="search"
          value={query}
          onChange={(e) => handleOnSearch(e.target.value)}
          placeholder="Cari resepi"
          className="input input-primary w-full md:w-1/2"
        />

        {query.length > 1 && (
          <p className="mt-2 font-medium max-w-lg overflow-clip w-full md:w-1/2">
            {allResepi.length} resepi dijumpai untuk kata kunci carian '{query}'
          </p>
        )}
      </div>

      <div className="mt-4 px-10 flex flex-col items-center">
        {query.length < 2 ? (
          <Card items={searchList} />
        ) : (
          <Card items={allResepi} />
        )}
      </div>

      <div className="mt-2 px-8 text-lg">
        <h3>Jumlah resepi terkini: {searchList.length}</h3>
      </div>
    </div>
  );
}

export default Search;
