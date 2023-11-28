from fastapi import FastAPI
import joblib
from  pydantic import BaseModel
import pandas as pd
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


#Endpoints

@app.get('/')
async def home():
    return {'Hello':'world'}

@app.post('/predict')
async def PredictSepsi(input:Sepsis_features):
    "function that receive the posted input data,do the operation and return an output /error message"
    output ={}   
    #try to execute the operation
    try:
        data = {
            'PRG': input.PRG,
            'PL':input.PL,
            'PR':input.PR,
            'SK':input.SK,
            'TS':input.TS,
            'M11':input.M11,
            'BD2':input.BD2,
            'Age':input.Age,
            'Insurance': input.Insurance,
        }
        
        df = pd.DataFrame([data])
        prediction = pipeline.predict(df)
        # print(f"[iNFO] Input data as dataframe:\n{prediction}")

        #Ml part
        if(prediction[0].tolist() ==0):
            response = "Negative"
        if(prediction[0].tolist() ==1 ):
            response ="Positive"
        # print(prediction)
        #format output
        output ={
            "data" : data,
            "operation" : "Addition",
            "way": "Sendind a data to predict",
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