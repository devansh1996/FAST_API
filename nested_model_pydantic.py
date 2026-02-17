from pydantic import BaseModel
class Patient(BaseModel):
    name:str
    age:int
    addres:'street house number city country' #complex
    address:Address #call the pydantic model address

class Address(BaseModel):
    house_no:int
    street:str
    city:str
    country:str
    pincode:int

address_dict={}
address1=Address(**address_dict)
patient_dict={}
patient1=Patient(**patient_dict)

print(patient1.address.pincode)