# Utility functions for the live trading bot

import logging
import os
from datetime import datetime

def setup_logging(log_file='trading_bot.log'):
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.info("Logging is set up.")

def log_trade(action, ticker, quantity, price):
    logging.info(f"{action} {quantity} of {ticker} at {price:.2f}")

def format_price(price):
    return f"${price:.2f}"

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def handle_error(error_message):
    logging.error(error_message)
    print(f"Error: {error_message}")