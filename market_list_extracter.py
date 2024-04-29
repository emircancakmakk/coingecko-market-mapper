import requests
import os

url = "https://api.coingecko.com/api/v3/exchanges/list"

headers = {
    "accept": "application/json",
    "x-cg-demo-api-key": os.getenv('COINGECKO_API_KEY')
}

response = requests.get(url, headers=headers)

for exchange in response.json():
    with open("market_list.txt", "a") as file:
        file.write(exchange["name"] + "\n")