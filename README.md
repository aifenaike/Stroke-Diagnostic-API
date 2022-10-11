# Stroke-Diagnostic-API
An API for Machine Learning powered diagnosis of stroke patients.


## Dataset Description
The [stroke](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset) dataset from kaggle is used to predict whether a patient is likely to get stroke based on the input parameters like `gender, age, various diseases, and smoking status`. Each row in the data provides relavant information about the patient.

| Feature      | Description |
| ----------- | ----------- |
| id          | unique identifier       |
| gender   | `Male`, `Female` or `Other`        |
| age     | age of the patient       |
| hypertension   | 0 if the patient doesn't have hypertension, 1 if the patient has hypertension        |
| heart_disease   | 0 if the patient doesn't have any heart diseases, 1 if the patient has a heart disease      |
| ever_married   | "No" or "Yes"        |
| work_type   | "children", "Govt_jov", "Never_worked", "Private" or "Self-employed"      |
