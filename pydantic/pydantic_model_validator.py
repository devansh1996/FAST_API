from pydantic import BaseModel,model_validator , EmailStr,AnyUrl,Field
from typing import List,Optional,Dict
## why we need typing : to not only check list
## but also inside the list is also str 

class Patient(BaseModel):
    name:str=Field(max_length=150)
    age:int=Field(gt=0,lt=120)
    email:EmailStr
    weight:float = Field(gt=0)
    linkedin:AnyUrl
    married:bool=False ## =false is the default value
    allergies: Optional[List[str]] = Field(max_length=5)
    contact_detail:Dict[str,str]   
    @model_validator(model='after')
    def validation_contact(cls,model):
        if model.age>60 and 'emergency' not in model.contact_detail:
            raise ValueError('patient old than 60 need emergency')
        else:
            return model

def insert_patient_data(patient:Patient):
    print(patient.age)
