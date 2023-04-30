FROM python:3.10

RUN apt install -y libpq-dev gcc

RUN mkdir model
WORKDIR /model

COPY . .

RUN chmod 777 ./app/model.xgb
RUN pip install -r ./requirements.txt

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080" ]
