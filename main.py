#Python built-in functions
from typing import Optional

#Pydantic 
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body

app = FastAPI() #Create an instance of FastAPI

#Creating a model
class Person(BaseModel):
    first_name: str
    surname: str
    age: int
    hair_colour: Optional[str] = None
    is_married: Optional[bool] = None

@app.get('/')   #Create a path operation
def home():     #Decorated by the line above
    return {'Hello': 'World'} #Return a JSON (dictionary)

#Request and response body

@app.post('/person/new')
def create_person(person: Person = Body(...)):
    return person
  