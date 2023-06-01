import React from "react";

type Props = {};

const Card = ({ items }) => {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-2 md:gap-4">
      {items.map((item: any) => (
        <div className="card rounded-md w-80 md:w-96 bg-base-100 shadow-md">
          <figure className="w-auto h-56">
            <img src={item.thumbnailUrl} alt="" />
          </figure>
          <div className="card-body p-4 font-base bg-transparent">
            <a href={item.url}>{item.content}</a>
          </div>
        </div>
      ))}
    </div>
  );
};

export default Card;
