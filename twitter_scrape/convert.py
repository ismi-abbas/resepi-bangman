# convert csv to json
import csv
import json

csvFilePath = "resepi_bangman.csv"
jsonFilePath = "resepi_bangman.json"

data = []
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        # modify each column name to match with json format
        csvRow["dateCreated"] = csvRow.pop("Date Created")
        csvRow["tweetId"] = csvRow.pop("Tweet ID")
        csvRow["content"] = csvRow.pop("Tweet Content")
        csvRow["index"] = csvRow.pop("")
        csvRow["url"] = csvRow.pop("URL")
        data.append(csvRow)

# write data to json file
with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(json.dumps(data, indent=2))
