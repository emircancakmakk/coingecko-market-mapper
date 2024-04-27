import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_page_data(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception if request fails
        return response.text
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None

def scrape_coin_market_data():
    for coin_id in range(1, 14031):
        base_url = f'https://www.coingecko.com/tr/coins/{coin_id}/markets/spot?page='
        page_number = 1
        
        while True:
            url = base_url + str(page_number)
            page_content = fetch_page_data(url)
            
            if not page_content:
                break
            
            soup = BeautifulSoup(page_content, 'html.parser')
            pagination_results = soup.find('div', class_='gecko-pagination-results')
            
            try:
                if pagination_results:
                    total_pages = int(pagination_results.text.strip().split()[0])
                    print(f"Scraping data for Coin ID: {coin_id}, Page: {page_number}/{total_pages}")
                    
                    table = soup.find('table')
                    if table:
                        parse_table_data(table)
                    
                    if page_number >= total_pages:
                        break
                    
                    page_number += 1
                else:
                    print("Pagination results not found.")
                    break
            except Exception as e:
                print(f"Error scraping data for Coin ID: {coin_id}, Page: {page_number}. Error: {e}")
                break

def parse_table_data(table):
    rows = table.find_all('tr')
    for row in rows:
        columns = row.find_all(['th', 'td'])
        row_data = [column.text.strip() for column in columns]
        print(row_data)

if __name__ == "__main__":
    scrape_coin_market_data()
