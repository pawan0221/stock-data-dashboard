import yfinance as yf
import pandas as pd

def fetch_stock(symbol):

    df = yf.download(
        symbol + ".NS",
        period="60d"
    )

    # Fix multi-index columns
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df.reset_index(inplace=True)

    df = df.ffill()

    # keep only required columns
    df = df[
        [
            "Date",
            "Open",
            "High",
            "Low",
            "Close",
            "Volume"
        ]
    ]

    return df