from pydantic import BaseModel ,field_validator, EmailStr,AnyUrl,Field
from typing import List,Optional,Dict
## why we need typing : to not only check list
## but also inside the list is also str 
 
##mode=before or after works AFTER or BEFORE TYPE COERCION 
class Patient(BaseModel):
    name:str=Field(max_length=150)
    age:int=Field(gt=0,lt=120)
    email:EmailStr
    weight:float = Field(gt=0)
    linkedin:AnyUrl
    married:bool=False ## =false is the default value
    allergies: Optional[List[str]] = Field(max_length=5)
    contact_detail:Dict[str,str]    
    @field_validator('email')
    @classmethod #is a class method for patient class
    def email_validator(cls,value):#pass class instance and value 
        valid_domain=['hdfc.com','icici.com']
        domain_name=value.split('@')[-1]
        if domain_name not in valid_domain:
            raise ValueError
    @field_validator('name',mode='before')
    @classmethod
    def transform_name(cls,value):
        return value.upper()



def insert_patient_data(patient:Patient):
    print(patient.age)
