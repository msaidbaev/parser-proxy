from fastapi import FastAPI

app = FastAPI()


@app.get('/model')
def predict():
    return {'success': True}
