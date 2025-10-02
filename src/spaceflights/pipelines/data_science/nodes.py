import typing as t
import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

logger = logging.getLogger(__name__)

def split_data(df: pd.DataFrame, parameters: t.Dict) -> t.Tuple:
    X = df[parameters['features']]
    y = df['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=parameters['test_size'])
    return X_train, X_test, y_train, y_test

def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> LinearRegression:
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    return regressor

def evaluate_model(regressor: LinearRegression, X_test=pd.DataFrame, y_test=pd.Series):
    y_pred = regressor.predict(X_test)
    score = r2_score(y_test, y_pred)
    logger.info(f"Model has a coefficient R^2 of {score:.3f} on test data")
    

