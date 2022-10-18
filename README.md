# Stroke-Diagnostic-API
This project describes a step-by-step procedure for deploying a machine learning powered RestAPI for stroke diagnosis using FastAPI and Docker.

## Motivation
The  purpose  of this project is to create an API for accurate medical diagnosis of `Stroke` using machine learning and individual patient's characteristics. Thus, providing useful information for the medical staff to deploy the needed treatment and decrease risks and consequences.

Stroke is a condition that occurs when the blood supply to the brain is interrupted or reduced due to a blockage (ischemic stroke) or rupture of a blood vessel (hemorrhagic stroke). Without blood, the brain will not get oxygen and nutrients, so cells in some areas of the brain will die. This condition causes parts of the body controlled by the damaged area of the brain to not function properly.

Stroke is an emergency condition that needs to be treated as soon as possible, because brain cells can die in just a matter of minutes. Prompt and appropriate treatment measures can minimize the level of brain damage and prevent possible complications.

In this machine learning project, the overall objective is to develop a system to predict the likelihood of a patient having a stroke based on several factors including: age, certain diseases (hypertension, heart disease). Thus helping medical professionals identify high risk patients.

As previously explained, stroke can kill a patient in a matter of minutes. Detecting stroke using the existing causative factors with the help of machine learning can be very useful to detect early tendecies of stroke in patients. 


## Dataset Description
The [stroke](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset) dataset from kaggle is used to predict whether a patient is likely to get stroke based on the input parameters like `gender, age, various diseases, and smoking status`. Each row in the data provides relavant information about the patient.

| Feature      | Description |
| ----------- | ----------- |
| **id**          | unique identifier       |
| **gender**   | `Male`, `Female` or `Other`        |
| **age**     | age of the patient       |
| **hypertension**   | 0 if the patient doesn't have hypertension, 1 if the patient has hypertension        |
| **heart_disease**   | 0 if the patient doesn't have any heart diseases, 1 if the patient has a heart disease      |
| **ever_married**   | `No` or `Yes`        |
| **work_type**   | `children`, `Govt_jov`, `Never_worked`, `Private` or `Self-employed`      |
| **Residence_type**   | `Rural` or `Urban`    |
| **avg_glucose_level**   | average glucose level in blood   |
| **bmi**   | body mass index      |
| **smoking_status**   | `formerly smoked`, `never smoked`, `smokes` or `Unknown`     |
| **stroke**   |  if the patient had a stroke or 0 if not    |


## Project Directory 
```bash
.
├── app
    └── Models                              > main fastapi app
        ├── RandomForest.pkl                > pickled random forest model
        └── preprocessing_pipeline.pkl      > Pickled preprocessing pipeline
    ├── utilities                           
    │   └── utility.py                      > Script containing helper function used in modeling and preprocessing
    ├── Dockerfile
    ├── docker-compose.yaml
    ├── input_validation.py                 > pydantic driven input validation
    ├── app.py                              > FastAPI app
    └── modeling.py                         > Model developmnet script
├── data                                    > Data directory
│   └── stroke_data.csv                     > stroke dataset
├── test                                    > set of tests
│   ├── config_test.py                      > centralized data registry tests
│   ├── test_api_server.py                  > FastAPI app tests
│   ├── test_inference.py                   > test for prediction/inference
│   └── test_preprocessing.py               > test for preprocessing pipeline
│
├── README.md                               > Documentation                       
└── requirements.txt                        > dependencies
```

## Benchmarks
- Successfully created a RESTful API using FastAPI, implementing the following:
  - A GET request on the root drives back to the `redocs` page by default.
  - A POST request that does model inference.
  - Type hinting was used.
  - Use a Pydantic model to ingest the body from POST. This model should contain an example.
  - Hint: the data has names with hyphens and Python does not allow those as variable names. We do not modify the column names in the csv and instead use the functionality of FastAPI/Pydantic/etc to deal with this.
-  Several unit tests to test the API (one for the GET and two for POST, one that tests each prediction).


## Build Docker Image

* You can build this docker image from the dockerfile using this command
```bash
cd app

docker-compose up
```
* You can then run the dockerized application on local host via port 8000:

```localhost:8000 This shows the documengtation page as default```

* You can interact with the APi on localhost via:
`localhost:8000/docs`


* Here are some screenshots:

<p align="center">
  <img width="600" height="400" src="https://github.com/aifenaike/Stroke-Diagnostic-API/blob/main/images/Screenshot%20(350).png">
</p>


<p align="center">
  <img width="600" height="400" src="https://github.com/aifenaike/Stroke-Diagnostic-API/blob/main/images/Screenshot%20(351).png">
</p>


<p align="center">
  <img width="600" height="400" src="https://github.com/aifenaike/Stroke-Diagnostic-API/blob/main/images/Screenshot%20(352).png">
</p>

* From the screenshot above, we diagnose a 24.4% tendency of having stroke.

## Technologies

For project the following tech stack, APIs, architecture was used and applied: 

* Python✅
* FastAPI ✅
* Docker Compose ✅
* sklearn ✅

## 1️⃣ UNIT TESTING

* In order for the unit testing to be successful we used a  *json loading*, so that the code is not hard coded only for the provided given data. 

* Therefore, during the unit testing (all the tests can be found under **/test**) we can now create *customer* and *loan* objects that are properly pushed to a local db (2 respective data tables). All the endpoints retrieve the necessary data from the provided json.

## 🔮 FUTURE WORK 

The areas of improvement in this projects includes:

* To build more endpoints
* To build an endpoint for extracting **feature importances** (eg. through the use of the LIME algorithm)
* To optimise **machine learning models** by experimenting (by properly storing the experiment configurations and results eg. Spreadsheet) - DVC/MLflow integration
* web Hosting 
