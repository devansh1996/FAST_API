from pydantic import BaseModel, computed_field, EmailStr,AnyUrl
from typing import List,Optional,Dict
## why we need typing : to not only check list
## but also inside the list is also str 

class Patient(BaseModel):
    name:str
    age:int
    email:EmailStr
    weight:float
    height:float
    linkedin:AnyUrl
    married:bool=False ## =false is the default value
    allergies: Optional[List[str]]
    contact_detail:Dict[str,str]   
    @computed_field
    @property
    def calculate_bmi(self)->float:
        bmi=self.weight/self.height 

def insert_patient_data(patient:Patient):
    print(patient.age)
