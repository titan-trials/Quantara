import pytest
from src.strategies.crossover import backtest_crossover

def test_backtest_crossover():
    # Test parameters
    ticker = 'AAPL'
    starting_cash = 100000
    shares_per_trade = 100
    use_ema = False
    start_date = '2025-01-01'
    end_date = '2025-10-01'

    # Run the backtest
    result = backtest_crossover(ticker, starting_cash, shares_per_trade, use_ema, start_date, end_date)

    # Assertions to validate the results
    assert result is not None
    assert result['Ticker'] == ticker
    assert result['Ending Cash'] >= 0
    assert isinstance(result['Buy Trades'], int)
    assert isinstance(result['Sell Trades'], int)
    assert isinstance(result['Realized Profit'], float) or isinstance(result['Realized Profit'], int)
    assert isinstance(result['ROI (%)'], float) or isinstance(result['ROI (%)'], int)