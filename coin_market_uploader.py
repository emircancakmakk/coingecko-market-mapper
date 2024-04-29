import os
import json
from supabase import create_client

supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

supabase = create_client(supabase_url, supabase_key)

try:
    markets_response = supabase.table('markets').select('id, name').execute()
    markets_dict = {market['name']: market['id'] for market in markets_response.data}

    coins_response = supabase.table('coins').select("id, name").execute()
    for coin in coins_response.data:
        coin_id = coin['id']
        coin_name = coin['name']
        
        with open(f'coins/{coin_name}.json') as f:
            data = json.load(f)
            coin_markets = data.get('markets', [])
            
            for coin_market in coin_markets:
                if coin_market in markets_dict:
                    market_id = markets_dict[coin_market]
                    
                    data, count = supabase.table('coinmarkets').insert({"coin_id": coin_id, "market_id": market_id}).execute()
                else:
                    print(f"Market '{coin_market}' not found in the database.")

    print("Data insertion completed successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
