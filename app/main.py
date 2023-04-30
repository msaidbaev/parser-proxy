from fastapi import FastAPI
import json
from xgboost import XGBClassifier

app = FastAPI()


@app.get('/model')
async def predict(data: str):
    data = json.loads(data)
    print(data)
    print(type(data))
    classifier = XGBClassifier()
    classifier.load_model('/model/app/model.xgb')
    prediction = classifier.predict([data]).tolist()
    return prediction[0]
