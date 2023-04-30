from fastapi import FastAPI
from xgboost import XGBClassifier

app = FastAPI()


@app.get('/model')
def predict():
    classifier = XGBClassifier()
    classifier.load_model('/model/app/model.xgb')
    prediction = classifier.predict([[1, 1, 1, 1, 0, 0, 0, 0, 2, 15, 427500.0, 32, 12.0, 4,	1, 0, 4, 18]]).tolist()
    return prediction[0]
