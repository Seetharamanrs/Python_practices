from pydantic import BaseModel
from fastapi import FastAPI

app=FastAPI()

class MedicalInput(BaseModel):
    age:int
    bmi:float
    children:int
    smoker:str
    region:str

@app.post("/predict")
def predict(data: MedicalInput):

    return {
            "message": "Data received successfully",
            "data": data
    }
