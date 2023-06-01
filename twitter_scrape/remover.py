import json


def clean_up_json(file_path):
    with open(file_path) as json_file:
        json_data = json.load(json_file)
        for data in json_data:
            # check for null thumbnailUrl
            if data["thumbnailUrl"] == "":
                # remove the data from json
                json_data.remove(data)
                # write data to json file
                with open(file_path, "w") as jsonFile:
                    jsonFile.write(json.dumps(json_data, indent=2))
            # check if content containt https://t.co/ - remove the https://t.co/ until end of line from content
            if "https://t.co/" in data["content"]:
                data["content"] = data["content"].split("https://t.co/")[0]
                # write data to json file
                with open(file_path, "w") as jsonFile:
                    jsonFile.write(json.dumps(json_data, indent=2))
