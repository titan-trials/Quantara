def calculate_sma(prices, window):
    """Calculate the Simple Moving Average (SMA) for a given price series."""
    return prices.rolling(window=window).mean()