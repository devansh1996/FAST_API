from pydantic import BaseModel , EmailStr,AnyUrl,Field
from typing import List,Optional,Dict,Annotated
## why we need typing : to not only check list
## but also inside the list is also str 

class Patient(BaseModel):
    name:str=Annotated[str,Field(max_length=50,title='Name of the patient',description='give name of patient',examples=['devansh','rahul'])]
    age:int
    email:EmailStr
    weight:float
    linkedin:AnyUrl
    married:Annotated[bool,Field(default=False,title="single or not")] ## =false is the default value
    allergies: Optional[List[str]]
    contact_detail:Dict[str,str]    

def insert_patient_data(patient:Patient):
    print(patient.age)
