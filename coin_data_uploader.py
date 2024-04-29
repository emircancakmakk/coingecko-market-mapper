from supabase import create_client, Client
import os
import json

supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

supabase = create_client(supabase_url, supabase_key)

folder_path = "coins"

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path) and filename.endswith(".json"):
        with open(file_path, 'r') as f:
            coin_data = json.load(f)
            coin_name = coin_data["id"]
            coin_website = coin_data["links"]["homepage"][0]
            coin_watchlist_portfolio_users = coin_data["watchlist_portfolio_users"]
            coin_market_cap_rank = coin_data["market_cap_rank"]
            coin_price_change_percentage_30d = coin_data["price_change_percentage_30d"]
            coin_price_change_percentage_60d = coin_data["price_change_percentage_60d"]
            coin_price_chance_percentage_200d = coin_data["price_change_percentage_200d"]
            coin_price_change_percentage_1y = coin_data["price_change_percentage_1y"]
            
            supabase.table("coins").insert({
                "name": coin_name,
                "website": coin_website,
                "watchlist_portfolio_users": coin_watchlist_portfolio_users,
                "market_cap_rank": coin_market_cap_rank,
                "price_change_percentage_30d": coin_price_change_percentage_30d,
                "price_change_percentage_60d": coin_price_change_percentage_60d,
                "price_change_percentage_200d": coin_price_chance_percentage_200d,
                "price_change_percentage_1y": coin_price_change_percentage_1y
            }).execute()
