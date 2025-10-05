# crossover.py

import pandas as pd
from indicators.ema import calculate_ema
from indicators.sma import calculate_sma
from broker.alpaca_client import AlpacaClient
import time

class CrossoverStrategy:
    def __init__(self, ticker, short_window=12, long_window=26, use_ema=False):
        self.ticker = ticker
        self.short_window = short_window
        self.long_window = long_window
        self.use_ema = use_ema
        self.client = AlpacaClient()
        self.position = 0

    def get_signals(self):
        data = self.client.get_historical_data(self.ticker)
        prices = pd.Series(data['close'])

        short_ma = calculate_ema(prices, self.short_window) if self.use_ema else calculate_sma(prices, self.short_window)
        long_ma = calculate_ema(prices, self.long_window) if self.use_ema else calculate_sma(prices, self.long_window)

        signals = []
        for i in range(1, len(prices)):
            if short_ma[i] > long_ma[i] and short_ma[i - 1] <= long_ma[i - 1]:
                signals.append('Buy')
            elif short_ma[i] < long_ma[i] and short_ma[i - 1] >= long_ma[i - 1]:
                signals.append('Sell')
            else:
                signals.append('Hold')

        return signals

    def execute_trades(self):
        while True:
            signals = self.get_signals()
            latest_signal = signals[-1]

            if latest_signal == 'Buy' and self.position == 0:
                self.client.place_order(self.ticker, 'buy', 1)  # Buy 1 share
                self.position = 1
                print(f'Bought 1 share of {self.ticker}')

            elif latest_signal == 'Sell' and self.position > 0:
                self.client.place_order(self.ticker, 'sell', 1)  # Sell 1 share
                self.position = 0
                print(f'Sold 1 share of {self.ticker}')

            time.sleep(60)  # Wait for a minute before checking again

if __name__ == "__main__":
    strategy = CrossoverStrategy(ticker='AAPL', short_window=12, long_window=26, use_ema=False)
    strategy.execute_trades()