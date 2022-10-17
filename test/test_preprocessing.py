import sys
sys.path.append('./') 
from utilities.utils import correct


def test_preprocessor(preprocessor,data):
    #clean input
    df = correct(data)
    #preprocess query parameters
    clean_data=preprocessor.transform(df)
    assert clean_data.shape[1] == 18