from fastapi import FastAPI
import joblib
from  pydantic import BaseModel
import pandas as pd
import numpy as np
import uvicorn
import logging

#load pipeline
pipeline  = joblib.load('toolkit/pipeline.joblib')
encoder  = joblib.load('toolkit/encoder.joblib')

# Configure logs
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#Config
app = FastAPI(
    title = 'Sepsis Prediction App',
    version = '0.0.1',
    description = 'This API will predict if a patient has Sepsis or not'
)

# Create class to define our input type
class Sepsis_features(BaseModel):
    PRG:int
    PL:int
    PR:int
    SK:int
    TS:int
    M11:float
    BD2:float
    Age:int
    Insurance:float


@app.get('/')
async def home():
    return {'Hello world'}


@app.post('/predict')
async def Predict_Sepsis(input:Sepsis_features):
    "function that receive the posted input data,do the operation and return an output /error message"
    output ={}   
 
    try:
        data = {[Sepsis_features.model_dump]}

        df = pd.DataFrame([data])
        prediction_probs = pipeline.predict_proba(df)
        prediction_class = pipeline.predict(df)

        if(prediction_class[0].tolist() ==0):
            response = "Negative"
        if(prediction_class[0].tolist() ==1 ):
            response ="Positive"

        output = {
            "data": data,
            "predicted_class": prediction_class[0].tolist(),
            "prediction": prediction_probs[0].tolist(),
            "result":response
        }

    except ValueError as e :
        logger.error(f"ValueError: {e}")
        output ={ "error":str(e)}
        
    except Exception as e :
        output ={"error ": f"OOps something went wrong :\n{e}"}
    
    finally:
        return output # output must be json serializable

if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)