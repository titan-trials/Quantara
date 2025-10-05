def calculate_ema(prices, window):
    """Calculate the Exponential Moving Average (EMA) for a given price series."""
    return prices.ewm(span=window, adjust=False).mean()