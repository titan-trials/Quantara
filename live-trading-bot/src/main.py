import time
import logging
from config import API_KEY, API_SECRET, BASE_URL
from broker.alpaca_client import AlpacaClient
from data.loader import DataLoader
from strategies.crossover import CrossoverStrategy

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    # Initialize Alpaca client
    alpaca_client = AlpacaClient(API_KEY, API_SECRET, BASE_URL)
    
    # Load market data
    data_loader = DataLoader(alpaca_client)
    
    # Initialize trading strategy
    strategy = CrossoverStrategy(data_loader)

    logging.info("Starting live trading bot...")

    while True:
        try:
            # Fetch market data
            market_data = data_loader.get_market_data()
            
            # Generate trading signals
            signals = strategy.generate_signals(market_data)
            
            # Execute trades based on signals
            for signal in signals:
                if signal['action'] == 'buy':
                    alpaca_client.place_order(signal['ticker'], signal['quantity'], 'buy')
                    logging.info(f"Placed buy order for {signal['quantity']} shares of {signal['ticker']}")
                elif signal['action'] == 'sell':
                    alpaca_client.place_order(signal['ticker'], signal['quantity'], 'sell')
                    logging.info(f"Placed sell order for {signal['quantity']} shares of {signal['ticker']}")
            
            # Sleep for a specified interval before the next iteration
            time.sleep(60)  # Adjust the sleep time as needed

        except Exception as e:
            logging.error(f"An error occurred: {e}")
            time.sleep(60)  # Wait before retrying

if __name__ == "__main__":
    main()