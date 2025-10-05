def calculate_macd(prices, short_window=12, long_window=26, signal_window=9):
    """
    Calculate the Moving Average Convergence Divergence (MACD) indicator.

    Parameters:
    prices (pd.Series): Series of prices.
    short_window (int): The short period for the MACD line.
    long_window (int): The long period for the MACD line.
    signal_window (int): The period for the signal line.

    Returns:
    pd.DataFrame: A DataFrame containing the MACD line, signal line, and MACD histogram.
    """
    # Calculate the short and long EMA
    short_ema = prices.ewm(span=short_window, adjust=False).mean()
    long_ema = prices.ewm(span=long_window, adjust=False).mean()

    # Calculate MACD line
    macd_line = short_ema - long_ema

    # Calculate signal line
    signal_line = macd_line.ewm(span=signal_window, adjust=False).mean()

    # Calculate MACD histogram
    macd_hist = macd_line - signal_line

    return pd.DataFrame({
        'MACD': macd_line,
        'Signal': signal_line,
        'Histogram': macd_hist
    })