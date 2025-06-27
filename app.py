import uvicorn
from fastapi import FastAPI
import numpy as np
import pickle
import pandas as pd
from pydantic import BaseModel

app = FastAPI()

class BankNote(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float
    

pickle_in=open("clf.pkl","rb")
clf=pickle.load(pickle_in)

@app.get('/')
def root_route():
    return {'Hello':'World'}

@app.post('/predict')
def predict(note: BankNote):
    features = [[note.variance, note.skewness, note.curtosis, note.entropy]]
    prediction = clf.predict(features)[0]

    result = "Fake note" if prediction > 0.5 else "Real Bank note"
    
    return {"prediction": result}

@app.get('/{name}')
def get_name(name: str):
    return {'msg': f'Hello, {name}'}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
