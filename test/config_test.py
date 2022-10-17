import pytest
from fastapi.testclient import TestClient
import pandas as pd

import sys
sys.path.append('./') 
from utilities.utils import load_estimator, correct
from app import app


    
@pytest.fixture
def preprocess_data(data):
    """Preprocess data"""
    preprocessor = load_estimator("preprocessing_pipeline.pkl")
    processed_data = preprocessor.transform(data)
    return processed_data


@pytest.fixture
def inference_data_neg():
    """
    Inference data sample for negative class (No stroke)
    """
    data_dict = {"gender": "Male", 
                "age":10,
                "hypertension": 0,
                "heart_disease": 0,
                "ever_married": "No",
                "work_type": "children",
                "Residence_type": "Rural",
                "avg_glucose_level": 59.49,
                "bmi": 18.3,
                "smoking_status":"Unknown"}

    df = pd.DataFrame(data_dict,index=[0])
    return df


@pytest.fixture
def inference_data_pos():
    """
    Inference data sample for positive class (has stroke)
    """
    data_dict = {"gender": "Male", 
                "age":67,
                "hypertension": 0,
                "heart_disease": 1,
                "ever_married": "Yes",
                "work_type": "Private",
                "Residence_type": "Urban",
                "avg_glucose_level": 228.69,
                "bmi": 36.6,
                "smoking_status":"formerly_smoked"}

    df = pd.DataFrame(data_dict,index=[0])
    return df

@pytest.fixture
def client():
    """
    Get dataset
    """
    api_client = TestClient(app)
    return api_client