import os
import json

# ! This code iterated over the 'cryptoforce.json' file in the "coins" folder and updated the 'markets' key in each file to contain only unique values.

folder_path = "coins"

for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        file_path = os.path.join(folder_path, filename)
        try:
            with open(file_path, 'r') as f:
                coin_data = json.load(f)
                
                if "markets" in coin_data:
                    markets = coin_data["markets"]
                    unique_markets = list(set(markets))
                    coin_data["markets"] = unique_markets
                    
                    with open(file_path, 'w') as fw:
                        json.dump(coin_data, fw, indent=4)
                        
                    print(f"Successfully updated markets in {filename}")
                else:
                    print(f"Warning: 'markets' key not found in {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
