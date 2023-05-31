import snscrape.modules.twitter as sntwitter

name = "aimansalim_"

for tweet in sntwitter.TwitterUserScraper("aimansalim_").get_items():
    print(tweet)
    media = tweet.media
    print(media)
