from fastapi import FastAPI

app = FastAPI() #Create an instance of FastAPI

@app.get('/')   #Create a path operation
def home():     #Decorated by the line above
    return {'Hello': 'World'} #Return a JSON (dictionary)