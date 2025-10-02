from kedro.pipeline import Pipeline, Node, pipeline
from .nodes import split_data, train_model, evaluate_model


def create_modeling_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        Node(
            func=split_data,
            inputs=['model_input_table', 'params:model_options'],
            outputs=['X_train', 'X_test', 'y_train', 'y_test'],
            name='split_data_node',
        ),
        Node(
            func=train_model,
            inputs=['X_train', 'y_train'],
            outputs='regressor',
            name='train_model_node',
        ),
        Node(
            func=evaluate_model,
            inputs=['regressor', 'X_test', 'y_test'],
            outputs=None,
            name='evaluate_model_node',
        ),
    ])


def create_pipeline(**kwargs) -> Pipeline:
    modelling_pipeline = create_modeling_pipeline()
    
    active_pipeline = pipeline(
        modelling_pipeline,
        inputs={"model_input_table": "model_input_table"},
        namespace="active_modeling_pipeline"
    )
    
    candidate_pipeline = pipeline(
        modelling_pipeline, 
        inputs={"model_input_table": "model_input_table"},
        namespace="candidate_modeling_pipeline"
    )

    return active_pipeline + candidate_pipeline