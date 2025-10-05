import os
import time
import pandas as pd
from alpaca_trade_api.rest import REST, TimeFrame
from config import API_KEY, API_SECRET, BASE_URL

class AlpacaClient:
    def __init__(self):
        self.api = REST(API_KEY, API_SECRET, BASE_URL)

    def get_market_data(self, symbol, start, end):
        try:
            bars = self.api.get_bars(symbol, TimeFrame.Day, start=start, end=end).df
            return bars
        except Exception as e:
            print(f"Error fetching market data for {symbol}: {e}")
            return pd.DataFrame()

    def place_order(self, symbol, qty, side, order_type='market', time_in_force='gtc'):
        try:
            order = self.api.submit_order(
                symbol=symbol,
                qty=qty,
                side=side,
                type=order_type,
                time_in_force=time_in_force
            )
            print(f"Order placed: {order}")
            return order
        except Exception as e:
            print(f"Error placing order for {symbol}: {e}")
            return None

    def get_account_info(self):
        try:
            account = self.api.get_account()
            return account
        except Exception as e:
            print(f"Error fetching account info: {e}")
            return None

    def run_live_trading(self, symbol, strategy, interval=60):
        while True:
            data = self.get_market_data(symbol, '2025-01-01', '2025-10-01')
            if not data.empty:
                signal = strategy.generate_signal(data)
                if signal == 'buy':
                    self.place_order(symbol, 1, 'buy')
                elif signal == 'sell':
                    self.place_order(symbol, 1, 'sell')
            time.sleep(interval)