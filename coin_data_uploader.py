import os
import json
from supabase import create_client

def main():
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
    if not supabase_url or not supabase_key:
        raise ValueError("Supabase URL or key is not provided.")

    supabase = create_client(supabase_url, supabase_key)

    folder_path = "coins"

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and filename.endswith(".json"):
            try:
                with open(file_path, 'r') as f:
                    coin_data = json.load(f)
                    if "id" not in coin_data or "links" not in coin_data or "homepage" not in coin_data["links"]:
                        print(f"Skipping {filename} due to missing required fields.")
                        continue

                    coin_name = coin_data["id"]
                    coin_website = coin_data["links"]["homepage"][0]
                    coin_watchlist_portfolio_users = coin_data.get("watchlist_portfolio_users", None)
                    coin_market_cap_rank = coin_data.get("market_cap_rank", None)
                    coin_price_change_percentage_30d = coin_data.get("price_change_percentage_30d", None)
                    coin_price_change_percentage_60d = coin_data.get("price_change_percentage_60d", None)
                    coin_price_change_percentage_200d = coin_data.get("price_change_percentage_200d", None)
                    coin_price_change_percentage_1y = coin_data.get("price_change_percentage_1y", None)

                    supabase.table("coins").insert({
                        "name": coin_name,
                        "website": coin_website,
                        "watchlist_portfolio_users": coin_watchlist_portfolio_users,
                        "market_cap_rank": coin_market_cap_rank,
                        "price_change_percentage_30d": coin_price_change_percentage_30d,
                        "price_change_percentage_60d": coin_price_change_percentage_60d,
                        "price_change_percentage_200d": coin_price_change_percentage_200d,
                        "price_change_percentage_1y": coin_price_change_percentage_1y
                    }).execute()
                    print(f"Inserted data for {coin_name}")
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")

if __name__ == "__main__":
    main()
