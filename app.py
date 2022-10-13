from fastapi import FastAPI
import uvicorn 
from utils import load_estimator

import numpy as np
import pandas as pd


app = FastAPI(debug=True)

@app.get('/')
def home():
    return {"text": "Stroke Prediction"}


@app.get("/predict")
def predict(gender:str, age:int, hypertension:int,
            heart_disease:str, ever_married:str, work_type:str,
            Residence_type:str, avg_glucose_level:float, bmi: float,
            smoking_status:str):


    df = pd.DataFrame({"gender":gender, "age":age, "hypertension":hypertension,
            "heart_disease":heart_disease, "ever_married":ever_married, "work_type":work_type,
            "Residence_type":Residence_type, "avg_glucose_level":avg_glucose_level, "bmi": bmi,
            "smoking_status":smoking_status},index=[0])

    preprocessor = load_estimator("preprocessing_pipeline.pkl")
    model = load_estimator("RandomForest.pkl")
    
    clean_data=preprocessor.transform(df)
    prediction = model.predict_proba(clean_data)
    prediction = np.squeeze(prediction)
    return { "Likelihood of having a Stroke": round(prediction[1],3)}

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)