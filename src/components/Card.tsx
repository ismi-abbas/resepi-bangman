const Card = ({ items }) => {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-2 md:gap-4">
      {items.map((item: any) => (
        <a href={item.url} key={item.tweetId} target="_blank">
          <div className="card rounded-md w-80 md:w-96 bg-base-100 shadow-md hover:ring-primary hover:ring-1">
            <figure className="w-auto h-56">
              <img src={item.thumbnailUrl} alt="" />
            </figure>
            <div className="card-body p-4 font-base bg-transparent">
              <p className="h-6 overflow-clip">{item.content}</p>
            </div>
          </div>
        </a>
      ))}
    </div>
  );
};

export default Card;
