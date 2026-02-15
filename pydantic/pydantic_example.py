from pydantic import BaseModel , EmailStr,AnyUrl
from typing import List,Optional,Dict
## why we need typing : to not only check list
## but also inside the list is also str 

class Patient(BaseModel):
    name:str
    age:int
    email:EmailStr
    weight:float
    linkedin:AnyUrl
    married:bool=False ## =false is the default value
    allergies: Optional[List[str]]
    contact_detail:Dict[str,str]    

def insert_patient_data(patient:Patient):
    print(patient.age)
