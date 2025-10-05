import pandas as pd
import matplotlib.pyplot as plt
import warnings
from datetime import datetime
from src.broker.alpaca_client import AlpacaClient
from src.indicators.ema import calculate_ema
from src.indicators.sma import calculate_sma
from src.indicators.macd import calculate_macd
from src.indicators.rsi import calculate_rsi
from src.indicators.dmi import calculate_dmi
from src.strategies.crossover import backtest_crossover
from src.config import API_KEY, API_SECRET

warnings.filterwarnings('ignore', category=UserWarning)

def run_backtest(ticker, start_date, end_date, starting_cash=100000, shares_per_trade=100, use_ema=False):
    alpaca_client = AlpacaClient(API_KEY, API_SECRET)
    
    print(f"Running backtest for {ticker} from {start_date} to {end_date}...")
    
    result = backtest_crossover(ticker, starting_cash, shares_per_trade, use_ema, start_date, end_date)
    
    if result is not None:
        print(f"Backtest completed for {ticker}.")
        print(f"Summary: {result}")
    else:
        print(f"Backtest failed for {ticker}.")

if __name__ == "__main__":
    tickers = ['AAPL', 'MSFT', 'GOOGL']  # Example tickers
    start_date = '2022-01-01'
    end_date = datetime.now().strftime('%Y-%m-%d')
    
    for ticker in tickers:
        run_backtest(ticker, start_date, end_date)