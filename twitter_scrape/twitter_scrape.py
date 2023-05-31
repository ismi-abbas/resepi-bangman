import snscrape.modules.twitter as sntwitter
import pandas as pd
import re

pattern = r"url='(.*?)'"

# Created a list to append all tweet attributes(data)
attributes_container = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i in enumerate(sntwitter.TwitterSearchScraper("from:@aimansalim_").get_items()):
    # find tweet that contain https://t.co/
    if "https://t.co/" in i[1].rawContent:
        attributes_container.append(
            [
                i[1].date,
                i[1].id,
                i[1].rawContent,
                i[1].user.renderedDescription,
                i[1].url,
                i[1].media,
            ]
        )

    if i[0] > 100:
        break


# Creating a dataframe from the tweets list above
tweets_df = pd.DataFrame(
    attributes_container,
    columns=[
        "Date Created",
        "Tweet ID",
        "Tweet Content",
        "Description",
        "URL",
        "Media",
    ],
)

# Converting dataframe to csv file order by created date
tweets_df.to_csv("twitter_bangman.csv", index=True, header=True)
