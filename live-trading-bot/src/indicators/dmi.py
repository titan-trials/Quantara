def calculate_dmi(df, period=14):
    """
    Calculate the Directional Movement Index (DMI) for a given DataFrame.

    Parameters:
    df (DataFrame): DataFrame containing 'high', 'low', and 'close' prices.
    period (int): The period over which to calculate the DMI.

    Returns:
    tuple: A tuple containing the positive and negative directional movement indicators.
    """
    high = df['high']
    low = df['low']
    close = df['close']

    # Calculate the True Range (TR)
    tr1 = high.diff()
    tr2 = low.diff()
    tr3 = close.shift(1) - high
    tr4 = close.shift(1) - low
    tr = pd.concat([tr1, tr2, tr3, tr4], axis=1).max(axis=1)
    tr = tr.fillna(0)

    # Calculate the Directional Movement (DM)
    up_move = high.diff()
    down_move = low.diff()

    +dm = (up_move.where((up_move > down_move) & (up_move > 0, 0)).rolling(window=period).sum())
    -dm = (down_move.where((down_move > up_move) & (down_move > 0, 0)).rolling(window=period).sum())

    # Calculate the smoothed True Range
    tr_smooth = tr.rolling(window=period).sum()

    # Calculate the Directional Indicators
    +di = (+dm / tr_smooth) * 100
    -di = (-dm / tr_smooth) * 100

    return +di, -di