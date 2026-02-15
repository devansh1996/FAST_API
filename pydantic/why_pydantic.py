## DEFINE A PYDANTIC MODEL WITH SCHEMA
## THEN PASS INSTANCE OF THIS MODEL 

##STEP 1: BUILD PYDANTIC MODEL 

from pydantic import BaseModel

class Patient(BaseModel):
    name:str
    age:int
    

patient_info={'name':'devansh','age':30}
patient1=Patient(**patient_info) ## object create

## object created with this info

## create instance and then update in database
## Define function using Class details
def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)

## pass patient info
insert_patient_data(patient1)
