import os
from supabase import create_client, Client

supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

supabase = create_client(supabase_url, supabase_key)

with open("market_list.txt", "r") as market_list:
    for market in market_list:
        market = market.strip()
        supabase.table("markets").insert({"name": market}).execute()
        print(f"Market '{market}' added to database.")
