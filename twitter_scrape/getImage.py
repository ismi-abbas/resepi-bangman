import snscrape.modules.twitter as sntwitter
from datetime import date

today = date.today().strftime("%Y-%m-%d")

name = "aimansalim_"

data = []

for tweet in sntwitter.TwitterUserScraper("aimansalim_").get_items():
    if "https://t.co/" in tweet.content:
        media = tweet.media
        print("tweet", tweet)
        print("media", media)
        print("id", tweet.id)

        data.append(
            [
                tweet.date,
                tweet.id,
                tweet.content,
                tweet.url,
                tweet.media,
            ]
        )
    if tweet[0] > 100:
        break

with open("tweets_bangman.txt", "a") as f:
    f.write(str(data) + "\n")
