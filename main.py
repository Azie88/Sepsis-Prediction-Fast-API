from fastapi import FastAPI
import joblib
from  pydantic import BaseModel
import pandas as pd
import uvicorn

#Config
app = FastAPI(
    title = 'Sepsis Prediction App',
    version = '0.0.1',
    description = 'This API will predict if a patient has Sepsis or not'
)

# # Create class to define our input type
# class input(BaseModel):
#     PRG:int
#     PL:int
#     PR:int
#     SK:int
#     TS:int
#     M11:float
#     BD2:float
#     Age:int
#     Insurance:float

@app.get('/')
async def hello_world():
    return {'Hello':'world'}

# @app.get('/info')
# def appinfo():
#     return 'This is the info page of this app'

# @app.post('/predict_grade')
# def predict_wine_grade(wine_features:WineFeatures):
#     df = pd.DataFrame()
#     prediction = pipeline.predict(df)[0]
#     return {'prediction':prediction}
