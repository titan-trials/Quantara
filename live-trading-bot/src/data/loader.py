import pandas as pd
from alpaca_trade_api.rest import REST, TimeFrame
from config import API_KEY, API_SECRET, BASE_URL

class DataLoader:
    def __init__(self):
        self.api = REST(API_KEY, API_SECRET, BASE_URL)

    def load_data(self, ticker, start_date, end_date):
        try:
            raw_data = self.api.get_bars(ticker, TimeFrame.Day, start=start_date, end=end_date).df
            if raw_data is None or raw_data.empty:
                raise ValueError(f"No data found for {ticker} between {start_date} and {end_date}.")
            return raw_data
        except Exception as e:
            print(f"Error loading data for {ticker}: {e}")
            return None

    def get_latest_data(self, ticker):
        try:
            latest_data = self.api.get_bars(ticker, TimeFrame.Day, limit=1).df
            if latest_data is None or latest_data.empty:
                raise ValueError(f"No latest data found for {ticker}.")
            return latest_data
        except Exception as e:
            print(f"Error fetching latest data for {ticker}: {e}")
            return None