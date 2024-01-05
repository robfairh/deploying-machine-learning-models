from feature_engine.imputation import CategoricalImputer, AddMissingIndicator, MeanMedianImputer
from regression_model.processing.features import ExtractLetterTransformer
from feature_engine.encoding import RareLabelEncoder, OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from regression_model.config.core import config
from sklearn.pipeline import Pipeline


# set up the pipeline
titanic_pipe = Pipeline([

    # ===== IMPUTATION =====
    # impute categorical variables with string 'missing'
    ('categorical_imputation', CategoricalImputer(
        imputation_method='missing', variables=config.model_config.CATEGORICAL_VARIABLES)),

    # add missing indicator to numerical variables
    ('missing_indicator', AddMissingIndicator(variables=config.model_config.NUMERICAL_VARIABLES)),

    # impute numerical variables with the median
    ('median_imputation', MeanMedianImputer(
        imputation_method='median', variables=config.model_config.NUMERICAL_VARIABLES)),

    # Extract first letter from cabin
    ('extract_letter', ExtractLetterTransformer(variables=config.model_config.CABIN)),

    # == CATEGORICAL ENCODING ======
    # remove categories present in less than 5% of the observations (0.05)
    # group them in one category called 'Rare'
    ('rare_label_encoder', RareLabelEncoder(tol=0.05, n_categories=1, variables=config.model_config.CATEGORICAL_VARIABLES)),

    # encode categorical variables using one hot encoding into k-1 variables
    ('categorical_encoder', OneHotEncoder(
        drop_last=True, variables=config.model_config.CATEGORICAL_VARIABLES)),

    # scale using standardization
    ('scaler', StandardScaler()),

    # logistic regression (use C=0.0005 and random_state=0)
    ('Logit', LogisticRegression()),
])