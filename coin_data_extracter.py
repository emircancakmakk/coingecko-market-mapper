import requests
from coin import Coin
import json
import time

headers = {
    "accept": "application/json"
}

with open("coin_ids.txt", "r") as coin_ids:
    for coin_id in coin_ids:
        coin_id = coin_id.strip()
        url = f"https://api.coingecko.com/api/v3/coins/{coin_id}?x_cg_demo_api_key=CG-REX7PBhEy3JQ9dhwV4CmrWkF"
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            coin_data = response.json()
            
            coin = Coin(coin_data)
            
            coin_data_extracted = {
                "id": coin_id,
                "links": coin.links,
                "watchlist_portfolio_users": coin.watchlist_portfolio_users,
                "market_cap_rank": coin.market_cap_rank,
                "price_change_percentage_30d": coin.price_change_percentage_30d,
                "price_change_percentage_60d": coin.price_change_percentage_60d,
                "price_change_percentage_200d": coin.price_change_percentage_200d,
                "price_change_percentage_1y": coin.price_change_percentage_1y,
                "markets": coin.markets,
                "chat_urls": coin.chat_urls
            }
            
            with open(f"coins/{coin_id}.json", "w", encoding="utf-8") as file:
                file.write(json.dumps(coin_data_extracted))
                
            print(f"Data for coin '{coin_id}' processed and saved to file.")
           
            time.sleep(2)
            
        except requests.exceptions.RequestException as e:
            with open("error_log.txt", "a") as error_log:
                error_log.write(f"Error fetching data for coin '{coin_id}': {e}\n")
            print(f"Error fetching data for coin '{coin_id}': {e}")
