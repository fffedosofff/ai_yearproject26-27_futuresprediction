"""One-node example of a Kedro pipeline."""

from kedro.pipeline import Pipeline, node

from .nodes import add_return_feature


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=add_return_feature,
                inputs="example_futures_prices",
                outputs="example_price_features",
                name="add_return_feature",
            )
        ]
    )
