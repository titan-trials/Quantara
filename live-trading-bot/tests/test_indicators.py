import pytest
from src.indicators.ema import calculate_ema
from src.indicators.sma import calculate_sma
from src.indicators.macd import calculate_macd
from src.indicators.rsi import calculate_rsi
from src.indicators.dmi import calculate_dmi
import pandas as pd

@pytest.fixture
def sample_data():
    data = {
        'close': [100, 102, 101, 105, 107, 106, 108, 110, 109, 111]
    }
    return pd.DataFrame(data)

def test_calculate_ema(sample_data):
    result = calculate_ema(sample_data['close'], window=3)
    expected = [None, None, 101.0, 103.0, 105.0, 105.0, 106.0, 107.0, 108.0, 109.0]
    pd.testing.assert_series_equal(result, pd.Series(expected, name='EMA'))

def test_calculate_sma(sample_data):
    result = calculate_sma(sample_data['close'], window=3)
    expected = [None, None, 101.0, 102.67, 104.0, 106.0, 107.0, 108.0, 109.0, 110.0]
    pd.testing.assert_series_equal(result, pd.Series(expected, name='SMA'))

def test_calculate_macd(sample_data):
    result = calculate_macd(sample_data['close'])
    expected = [None, None, None, None, None, None, None, None, None, None]  # Replace with actual expected values
    pd.testing.assert_series_equal(result, pd.Series(expected, name='MACD'))

def test_calculate_rsi(sample_data):
    result = calculate_rsi(sample_data['close'], window=14)
    expected = [None] * 10  # Replace with actual expected values
    pd.testing.assert_series_equal(result, pd.Series(expected, name='RSI'))

def test_calculate_dmi(sample_data):
    result_plus, result_minus = calculate_dmi(sample_data, period=14)
    expected_plus = [None] * 10  # Replace with actual expected values
    expected_minus = [None] * 10  # Replace with actual expected values
    pd.testing.assert_series_equal(result_plus, pd.Series(expected_plus, name='+DM'))
    pd.testing.assert_series_equal(result_minus, pd.Series(expected_minus, name='-DM'))