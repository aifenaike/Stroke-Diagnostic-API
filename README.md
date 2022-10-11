# Stroke-Diagnostic-API
An API for Machine Learning powered diagnosis of stroke patients. This project describes a step-by-step procedure for deploying a machine learning powered RestAPI for stroke diagnosis using FastAPI and Docker.

## Motivation
The  purpose  of this project is to create an API for accurate model diagnosis of `Stroke` using machine learning and individual patient's characteristics. Thus, providing useful information for the medical staff to deploy the needed treatment and decrease risks and consequences.

Stroke is a condition that occurs when the blood supply to the brain is interrupted or reduced due to a blockage (ischemic stroke) or rupture of a blood vessel (hemorrhagic stroke). Without blood, the brain will not get oxygen and nutrients, so cells in some areas of the brain will die. This condition causes parts of the body controlled by the damaged area of the brain to not function properly.

Stroke is an emergency condition that needs to be treated as soon as possible, because brain cells can die in just a matter of minutes. Prompt and appropriate treatment measures can minimize the level of brain damage and prevent possible complications.

In this machine learning project, the overall objective is to develop a systme to predict the likelihood of a patient having a stroke based on several factors including: age, certain diseases (hypertension, heart disease). Thus helping medical professionals identify high risk patients.

As previously explained, stroke can kill the sufferer in a matter of minutes. Detecting stroke with the existing causative factors with the help of machine learning can be very useful in the world of health to detect stroke early in order to increase the sense of heart among sufferers so that strokes can be prevented early.


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
