from fastapi import FastAPI, Request
import uvicorn 
import starlette.responses as _responses
from fastapi.responses import JSONResponse
from input_validation import input_data
from utilities.utils import load_estimator, run_inference
import pandas as pd

# Instatiate the FastAPI object
app = FastAPI(debug=True, title="fastapi-apptst",

    version=0.1,

    root_path="/")

# @app.get('/')
# def home():
#     return {"objective": "Stroke Prediction"}

# Index route, opens automatically on redocs
@app.get("/")
async def root():
    return _responses.RedirectResponse("/redoc")

#Set custom exception (400) error for wrong inputs/datatypes of fields
@app.exception_handler(ValueError)
async def value_error_exception_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)},
    )


#Prediction route
@app.post("/predict")
async def predict(data: input_data):
        
    df = pd.DataFrame(data.dict(),index=[0])
    preprocessor = load_estimator("preprocessing_pipeline.pkl")
    model = load_estimator("RandomForest.pkl")
    prediction = run_inference(preprocessor,model,df)
    return { "Likelihood of having a Stroke": round(prediction[1],3)}


# load the API with uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
