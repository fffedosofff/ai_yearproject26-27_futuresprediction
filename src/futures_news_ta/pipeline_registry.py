"""Register the project's Kedro pipelines."""

from kedro.pipeline import Pipeline

from futures_news_ta.pipelines.example import create_pipeline


def register_pipelines() -> dict[str, Pipeline]:
    example = create_pipeline()
    return {"__default__": example, "example": example}
