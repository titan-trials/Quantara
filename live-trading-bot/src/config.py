# Configuration settings for the trading bot

API_KEY = "your_api_key_here"
API_SECRET = "your_api_secret_here"
BASE_URL = "https://paper-api.alpaca.markets"  # Change to live URL for live trading

# Trading parameters
STARTING_CASH = 100000
SHARES_PER_TRADE = 100
SHORT_WINDOW = 12
LONG_WINDOW = 26
USE_EMA = False  # Set to True to use EMA instead of SMA

# Timeframe for trading
TIMEFRAME = "1D"  # Daily data

# RSI settings
RSI_WINDOW = 14
RSI_OVERSOLD = 35
RSI_OVERBOUGHT = 65

# Other settings
LOGGING_ENABLED = True
ERROR_HANDLING_ENABLED = True