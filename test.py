import pandas as pd
import requests
import json

# how to json uri convert to json file
url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Convert response to json format

    # Save json to a file
    with open("data.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)

    print("JSON data saved as data.json")
else:
    print("Failed to fetch data. Status code:", response.status_code)


# how to json uri data convert to csv file
url = "https://your-json-api.com/data"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    df = pd.json_normalize(data)
    df.to_csv("data.csv", index=False)
    print("JSON data saved as data.csv")
else:
    print("Failed to fetch data")

