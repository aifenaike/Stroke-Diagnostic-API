import pickle

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

def correct(df):
    df.gender = df.gender.str.title()
    df.ever_married = df.ever_married.str.title()
    df.Residence_type = df.Residence_type.str.title()
    return df
