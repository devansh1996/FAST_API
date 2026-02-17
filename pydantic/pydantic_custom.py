from pydantic import BaseModel , EmailStr,AnyUrl,Field
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

def insert_patient_data(patient:Patient):
    print(patient.age)
