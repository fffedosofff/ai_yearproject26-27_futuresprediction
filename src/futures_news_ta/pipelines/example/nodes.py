"""Example feature calculation; replace with research pipelines later."""

import pandas as pd


def add_return_feature(prices: pd.DataFrame) -> pd.DataFrame:
    """Sort price bars in UTC and calculate the previous bar's close return."""
    result = prices[["timestamp", "close"]].copy()
    result["timestamp"] = pd.to_datetime(result["timestamp"], utc=True)
    result["close"] = pd.to_numeric(result["close"])
    result = result.sort_values("timestamp").reset_index(drop=True)
    result["return_1"] = result["close"].pct_change()
    return result.dropna(subset=["return_1"]).reset_index(drop=True)
