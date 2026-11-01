"""Check that the example feature uses bars in time order."""

import pandas as pd
import pytest

from futures_news_ta.pipelines.example.nodes import add_return_feature


def test_add_return_feature_sorts_bars() -> None:
    prices = pd.DataFrame(
        {
            "timestamp": ["2026-10-01T11:00:00Z", "2026-10-01T10:00:00Z"],
            "close": [101.0, 100.0],
        }
    )

    features = add_return_feature(prices)

    assert len(features) == 1
    assert features.loc[0, "close"] == 101.0
    assert features.loc[0, "return_1"] == pytest.approx(0.01)
    assert str(features.loc[0, "timestamp"].tzinfo) == "UTC"


def test_add_return_feature_does_not_change_raw_prices() -> None:
    prices = pd.DataFrame(
        {
            "timestamp": ["2026-10-01T10:00:00Z", "2026-10-01T11:00:00Z"],
            "close": [100.0, 101.0],
        }
    )
    original = prices.copy(deep=True)

    add_return_feature(prices)

    pd.testing.assert_frame_equal(prices, original)
