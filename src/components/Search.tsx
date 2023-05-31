import Fuse from "fuse.js";
import { useState } from "react";
import React from "react";

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

      <div className="mt-4 px-10">
        {query.length < 2 ? (
          <div>
            {searchList.map((item: any) => (
              <li key={item.tweetId}>
                <a
                  href={item.url}
                  target="_blank"
                  className="hover:underline-offset-2 hover:underline text-lg"
                >
                  {item.content}
                </a>
              </li>
            ))}
          </div>
        ) : (
          <div>
            {allResepi &&
              allResepi.map((resepi: any) => (
                <li>
                  <a
                    href={`/${resepi?.url}`}
                    target="_blank"
                    className="hover:underline-offset-2 hover:underline text-lg"
                  >
                    {resepi.content}
                  </a>
                </li>
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
