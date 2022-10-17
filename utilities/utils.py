import pickle
import numpy as np

#save models and transformers
def save_estimator(file_name,model):
    # create an iterator object with write permission - model.pkl
    with open(f'Models/{file_name}', 'wb') as files:
        pickle.dump(model, files)
        
#load models and transformers
def load_estimator(file_name):
    # load saved model
    with open(f'Models/{file_name}' , 'rb') as f:
        model = pickle.load(f)
    return model

#Clean data
def correct(df):
    df.gender = df.gender.str.title()
    df.ever_married = df.ever_married.str.title()
    df.Residence_type = df.Residence_type.str.title()
    return df


#Predict
def run_inference(preprocessor,model,df):
    """Run Inference and return predicted probabilities"""
    df = correct(df)
    #preprocess query parameters
    clean_data=preprocessor.transform(df)
    
    #return prediction
    prediction = model.predict_proba(clean_data)
    prediction = np.squeeze(prediction)
    return prediction