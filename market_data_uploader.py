from supabase import create_client, Client

supabase_url = "https://bbicjwabaozinexagdeb.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJiaWNqd2FiYW96aW5leGFnZGViIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTQzNTA3MjgsImV4cCI6MjAyOTkyNjcyOH0.5If9CvcSC8F9oA8DS8xE62PC9hrlyfcipPIXiUriQ9Y"

supabase = create_client(supabase_url, supabase_key)

with open("market_list.txt", "r") as market_list:
    for market in market_list:
        market = market.strip()
        supabase.table("markets").insert({"name": market}).execute()
        print(f"Market '{market}' added to database.")
