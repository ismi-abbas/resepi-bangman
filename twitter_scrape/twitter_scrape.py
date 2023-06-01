import snscrape.modules.twitter as sntwitter
import pandas as pd
import convert_to
import remover

attributes_container = []

print("Scraping twitter...")
for i in enumerate(sntwitter.TwitterSearchScraper("from:@aimansalim_").get_items()):
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

    if i[0] > 10000:
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

# Converting csv file to json file
print("Converting csv to json...")
convert_to.convert_csv_to_json("twitter_bangman.csv", "twitter_bangman.json")

# Clean up json file
print("Cleaning up json...")
remover.clean_up_json("twitter_bangman.json")
