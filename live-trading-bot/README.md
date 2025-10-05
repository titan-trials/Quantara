# Live Trading Bot

This project is a live trading bot that continuously runs to generate buy and sell signals based on various trading strategies. It utilizes market indicators to inform trading decisions and interacts with the Alpaca API for executing trades.

## Project Structure

```
live-trading-bot
├── src
│   ├── main.py                # Entry point for the live trading bot
│   ├── config.py              # Configuration settings for the bot
│   ├── executor.py            # Manages order execution
│   ├── utils.py               # Utility functions
│   ├── broker
│   │   └── alpaca_client.py   # Alpaca API client implementation
│   ├── data
│   │   └── loader.py          # Market data loader
│   ├── indicators
│   │   ├── __init__.py        # Initializes the indicators module
│   │   ├── ema.py             # Exponential Moving Average (EMA) implementation
│   │   ├── sma.py             # Simple Moving Average (SMA) implementation
│   │   ├── macd.py            # Moving Average Convergence Divergence (MACD) implementation
│   │   ├── rsi.py             # Relative Strength Index (RSI) implementation
│   │   └── dmi.py             # Directional Movement Index (DMI) implementation
│   └── strategies
│       └── crossover.py       # Crossover trading strategy implementation
├── scripts
│   ├── run_live.sh            # Script to start the live trading bot
│   └── run_backtest.py        # Script to run backtests on historical data
├── tests
│   ├── test_indicators.py     # Unit tests for indicators
│   └── test_strategy.py       # Unit tests for trading strategies
├── .env.example                # Template for environment variables
├── requirements.txt            # Python dependencies
├── pyproject.toml             # Project configuration
├── Dockerfile                  # Docker image instructions
├── .gitignore                  # Git ignore file
└── README.md                   # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd live-trading-bot
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Configure your environment:**
   - Copy `.env.example` to `.env` and fill in your API keys and other settings.

5. **Run the live trading bot:**
   ```
   ./scripts/run_live.sh
   ```

## Usage

The bot will continuously monitor the market, generate buy and sell signals based on the defined strategies, and execute trades through the Alpaca API. You can modify the trading strategies and indicators as needed by editing the respective files in the `src` directory.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.