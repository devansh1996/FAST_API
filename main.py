import json
from fastapi import FastAPI,Path,Query,HTTPException
from fastapi.responses import JSONResponse
from typing import Annotated,Literal,Optional
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
        elif self.bmi>=25:
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

class PatientUpdate(BaseModel):
    id:str
    age:Annotated[Optional[int],Field(default=None)]
    name:Annotated[Optional[str],Field(default=None)]
    city:Annotated[Optional[str],Field(default=None)]
    gender:Annotated[Optional[Literal['Male','Female','Others']],Field(default=None)]
    height:Annotated[Optional[float],Field(default=None)]
    weight:Annotated[Optional[float],Field(default=None)]



@app.put('/edit/{patient_id}')
def update_date(patient_id:str,patient_update:PatientUpdate):
    data=load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404,detail='patient not found')
    existing_patient_info=data[patient_id]
    updated_patient_info=patient_update.model_dump(exclude_none=True) # important to include FIELDS MEANT TO UPDATE NOT ALL

    for key,value in updated_patient_info.items():
        existing_patient_info[key]=value
    ## convert exisint_patient_info to patient object
    ## so bmi is recalculated with the new value
    existing_patient_info['id']=patient_id
    patient_update_pydantic_obj=Patient(**existing_patient_info)
    ## converting this back to dictionary because bmi is calculated
    existing_patient_info= patient_update_pydantic_obj.model_dump(exclude='id')
    data[patient_id]=existing_patient_info
    #save data
    save_data(data)
    return JSONResponse(status_code=200,content='updated')


def save_data(data):
    with open('patients.json','w') as f:
        json.dump(data,f)