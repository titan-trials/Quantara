import time
import logging
from broker.alpaca_client import AlpacaClient
from strategies.crossover import CrossoverStrategy
from config import API_KEY, API_SECRET, BASE_URL, TRADE_SYMBOL, TRADE_QUANTITY

logging.basicConfig(level=logging.INFO)

class LiveTradingBot:
    def __init__(self):
        self.client = AlpacaClient(API_KEY, API_SECRET, BASE_URL)
        self.strategy = CrossoverStrategy(self.client)

    def run(self):
        logging.info("Starting live trading bot...")
        while True:
            try:
                self.strategy.generate_signals()
                self.execute_trades()
                time.sleep(60)  # Wait for a minute before the next iteration
            except Exception as e:
                logging.error(f"Error in live trading loop: {e}")
                time.sleep(60)  # Wait before retrying

    def execute_trades(self):
        signals = self.strategy.get_signals()
        for signal in signals:
            if signal['action'] == 'buy':
                self.client.place_order(symbol=TRADE_SYMBOL, qty=TRADE_QUANTITY, side='buy')
                logging.info(f"Placed buy order for {TRADE_QUANTITY} shares of {TRADE_SYMBOL}.")
            elif signal['action'] == 'sell':
                self.client.place_order(symbol=TRADE_SYMBOL, qty=TRADE_QUANTITY, side='sell')
                logging.info(f"Placed sell order for {TRADE_QUANTITY} shares of {TRADE_SYMBOL}.")

if __name__ == "__main__":
    bot = LiveTradingBot()
    bot.run()