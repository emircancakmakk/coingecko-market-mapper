class Coin:
    def __init__(self, coin_data):
        self.id = coin_data.get('id')
        self.links = coin_data.get('links', {})
        self.watchlist_portfolio_users = coin_data.get('watchlist_portfolio_users')
        self.market_cap_rank = coin_data.get('market_cap_rank')
        self.price_change_percentage_30d = coin_data.get('price_change_percentage_30d')
        self.price_change_percentage_60d = coin_data.get('price_change_percentage_60d')
        self.price_change_percentage_200d = coin_data.get('price_change_percentage_200d')
        self.price_change_percentage_1y = coin_data.get('price_change_percentage_1y')
        self.tickers = coin_data.get('tickers', [])
        self.markets = []
        self.chat_urls = []
        self.set_market_list()
        self.set_chat_urls()

    def set_market_list(self):
        for ticker in self.tickers:
            market = ticker.get('market', {}).get('name')
            if market:
                self.markets.append(market)

    def set_chat_urls(self):
        self.chat_urls = self.links.get('chat_url', [])