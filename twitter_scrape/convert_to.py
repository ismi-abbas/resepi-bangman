# convert csv to json
import csv
import json
import re

pattern = r"thumbnailUrl='(.*?)'"


def convert_csv_to_json(csvFilePath, jsonFilePath):
    data = []
    with open(csvFilePath) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for csvRow in csvReader:
            matches = re.findall(pattern, csvRow["Media"])
            if len(matches) > 0:
                csvRow["thumbnailUrl"] = matches[0]
            else:
                csvRow["thumbnailUrl"] = ""
            # modify each column name to match with json format
            csvRow["dateCreated"] = csvRow.pop("Date Created")
            csvRow["tweetId"] = csvRow.pop("Tweet ID")
            csvRow["content"] = csvRow.pop("Tweet Content")
            csvRow["index"] = csvRow.pop("")
            csvRow["url"] = csvRow.pop("URL")
            csvRow.pop("Media")
            csvRow.pop("Description")
            data.append(csvRow)

    # write data to json file
    with open(jsonFilePath, "w") as jsonFile:
        jsonFile.write(json.dumps(data, indent=2))
