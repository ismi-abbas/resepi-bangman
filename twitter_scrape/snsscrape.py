import snscrape.modules.twitter as sntwitter
import pandas as pd

# Created a list to append all tweet attributes(data)
attributes_container = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i in enumerate(sntwitter.TwitterSearchScraper("from:@aimansalim_").get_items()):
    print("Running... on" + str(i[0]) + "tweets")
    # find tweet that contain https://t.co/
    if "https://t.co/" in i[1].rawContent:
        attributes_container.append(
            [
                i[1].date,
                i[1].id,
                i[1].rawContent,
                i[1].user.renderedDescription,
                i[1].url,
            ]
        )

    if i[0] > 100000:
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
    ],
)

# Converting dataframe to csv file order by created date
tweets_df.to_csv("resepi_bangman.csv", index=True, header=True)
