from kedro.pipeline import Pipeline, pipeline, node
from .nodes import preprocess_companies,preprocess_shuttles

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        (node(
            func=preprocess_companies,
            inputs='companies',
            outputs='preprocessed_companies',
            name='preprocess_companies_node',
        )),
        (node(
            func=preprocess_shuttles,
            inputs='shuttles',
            outputs='preprocessed_shuttles',
            name='preprocess_shuttles_node',
        )),
    ])
