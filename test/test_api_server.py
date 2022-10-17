#test GET request
def test_get(client):
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "Greetings!"}

#test POST request
def test_post_high(client):
    request = client.post("/", json={"gender": "Male", 
                                        "age":10,
                                        "hypertension": 0,
                                        "heart_disease": 0,
                                        "ever_married": "No",
                                        "work_type": "children",
                                        "Residence_type": "Rural",
                                        "avg_glucose_level": 59.49,
                                        "bmi": 18.3,
                                        "smoking_status":"Unknown"
                                     })
    assert request.status_code == 200
    assert 0 <= request.json()["Likelihood of having a Stroke"] <= 1.0

#Test bad request ===> Wrong category specified for categorical variables
def test_post_malformed(client):
    r = client.post("/", json={
                "gender": "MaleMale", 
                "age":10,
                "hypertension": 0,
                "heart_disease": 0,
                "ever_married": "No",
                "work_type": "children",
                "Residence_type": "Rural",
                "avg_glucose_level": 59.49,
                "bmi": 45.2,
                "smoking_status":"Unknown"
    })
    assert r.status_code == 400
