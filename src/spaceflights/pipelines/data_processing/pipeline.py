from kedro.pipeline import Pipeline, pipeline, node, Node
from .nodes import preprocess_companies,preprocess_shuttles, create_model_input_table

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        Node(
            func=preprocess_companies,
            inputs='companies',
            outputs='preprocessed_companies',
            name='preprocess_companies_node',
        ),
        Node(
            func=preprocess_shuttles,
            inputs='shuttles',
            outputs='preprocessed_shuttles',
            name='preprocess_shuttles_node',
        ),
        Node(
            func=create_model_input_table,
            inputs=['preprocessed_companies', 'preprocessed_shuttles', 'reviews'],
            outputs='model_input_table',
            name='create_model_input_table_node'
        ),
    ])
