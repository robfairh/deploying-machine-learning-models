import numpy as np
from regression_model.config.core import config
from regression_model.processing.features import ExtractLetterTransformer


# def test_temporal_variable_transformer(sample_input_data):
#     # Given
#     transformer = TemporalVariableTransformer(
#         variables=config.model_config.temporal_vars,  # YearRemodAdd
#         reference_variable=config.model_config.ref_var,
#     )
#     assert sample_input_data["YearRemodAdd"].iat[0] == 1961

#     # When
#     subject = transformer.fit_transform(sample_input_data)

#     # Then
#     assert subject["YearRemodAdd"].iat[0] == 49

def test_extract_letter_transformer(sample_input_data):
    # Given
    transformer = ExtractLetterTransformer(
        variables=config.model_config.CABIN,
    )
    assert np.isnan(sample_input_data["cabin"].iat[0])
    # print(sample_input_data["cabin"].iat[0])

    # When
    subject = transformer.fit_transform(sample_input_data)

    # Then
    assert np.isnan(subject["cabin"].iat[0])
    # print(sample_input_data["cabin"].iat[0])
