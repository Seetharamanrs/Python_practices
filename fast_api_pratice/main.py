from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return {"message":"Hello FastAPI"}
@app.get("/profile")
def profile():
    return{
        "name":"Seetharaman",
        "role":"AI/Ml engineer"
    }
@app.get("/skills")
def skills():
    return{
        "skills":["python","SQL","FastAPI"]
    }
@app.get("/patient/{patient_id}")
def patient(patient_id:int):
    return {
        "patient_id":patient_id
    }
@app.get("/insurance")
def insurance(age:int,bmi:int):
    return {
        "age":age,
        "bmi":bmi
    }
@app.get("/model/{model_name}")
def model(model_name):
    return {
        "model":model_name
    }
