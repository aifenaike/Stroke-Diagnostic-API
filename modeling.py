#Import relevant packages
import numpy as np
import pandas as pd

import sklearn
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import log_loss

import warnings
warnings.filterwarnings('ignore')
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

#Read dataset
data = pd.read_csv("data/stroke_data.csv")

#correct data type for age
data['age'] = data['age'].astype(np.int64)

#seperate predictors from target feature.
input_features = data.drop(['stroke'],1)
target = data['stroke']

#split data into training and testing sets
Train, Test, train_target, test_target = train_test_split(input_features,target,test_size=0.2,random_state=34)

#Encode categorical features
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,OrdinalEncoder

cat_encoder = ColumnTransformer(transformers = [("lb_encoder",OrdinalEncoder(),[1,5,7]),
                                ('ohe_encoder', OneHotEncoder(),[6,10])],
                                remainder ='passthrough')

#Missing value imputation by mean
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='mean')

#Chain into a single pipeline
from sklearn.pipeline import Pipeline
preprocessing_pipeline = Pipeline([('encoder', cat_encoder), ('imputer', imputer)])

Train_features = preprocessing_pipeline.fit_transform(Train)
Test_features = preprocessing_pipeline.transform(Test)

#save pipeline
save_estimator(file_name="preprocessing_pipeline.pkl",model=preprocessing_pipeline)

#Oversampling the minority class
from imblearn.over_sampling import SMOTE
# transform the dataset
oversample = SMOTE(random_state=2)
Train_features, train_target = oversample.fit_resample(Train_features, train_target)


#Random Forest Classifier
Rf_model =RandomForestClassifier(random_state=23,n_jobs=-1,n_estimators= 500,
                                   min_samples_split= 2,max_features="auto",max_depth=9)
Rf_model.fit(Train_features, train_target)
#Test model performance oon training and test sets
train_predictions =Rf_model.predict_proba(Train_features)[:,1]
test_predictions = Rf_model.predict_proba(Test_features)[:,1]

print(f"Logloss for training set: {log_loss(train_target,train_predictions)}")
print(f"Logloss for testing set: {log_loss(test_target,test_predictions)}")

#save Model
save_estimator(file_name="RandomForest.pkl",model=Rf_model)


