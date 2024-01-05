# import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class ExtractLetterTransformer(BaseEstimator, TransformerMixin):
    # Extract fist letter of variable

    def __init__(self, variables):
        if not isinstance(variables, list):
            raise ValueError('variables should be a list')

        self.variables = variables

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # so that we do not over-write the original dataframe
        X = X.copy()

        for variable in self.variables:
            X[variable] = X[variable].str[0]
        return X
