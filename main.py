import json
from fastapi import FastAPI,Path,Query,HTTPException
from fastapi.responses import JSONResponse
from typing import Annotated,Literal
import pydantic
from pydantic import BaseModel,Field,computed_field
app=FastAPI()

class Patient(BaseModel):
    id:str
    age:Annotated[int,Field(...,description='Age of the patient',examples=['33'],gt=0,lt=100)]
    name:Annotated[str,Field(...,description='name of the patient')]
    city:Annotated[str,Field(...,description='City')]
    gender:Annotated[Literal['Male','Female','Others'],Field(...,description='Gender')]
    height:Annotated[float,Field(...,gt=0,description='Height of patient')]
    weight:Annotated[float,Field(...,gt=0,description='Weight of patient')]
    @computed_field
    @property
    def bmi(self)->float:
        bmi=round((self.weight/self.height),2)
        return bmi
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi<18.5:
            return 'underweight'
        elif self.bmi<25:
            return 'normal'
        elif self.bmi>25:
            return 'overweight'
        
def load_data():
    with open('patients.json','r') as f:
        data=json.load(f)
    return data
@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/about")
def hello():
    return {'message':'Hello World'}

@app.get('/view')
def view():
    data=load_data()
    return data


@app.post("/create")
def create_patient(patient:Patient):
    ## load data
    data=load_data()

    ## check if patient exists
    if patient.id in data:
        raise HTTPException(status_code=400,detail='patient already exists')

    ## new patient add
    data[patient.id]=patient.model_dump(exclude=['id'])

    ## save into json
    save_data(data) 
    return JSONResponse(status_code=201,content={'message':'patient create successfully'})

def save_data(data):
    with open('patients.json','w') as f:
        json.dump(data,f)