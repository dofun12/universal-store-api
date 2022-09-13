import json

from fastapi import FastAPI, Request

from src.database.db_manager import DBManager

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/store/{db_name}/{collection}")
async def list_all(db_name: str, collection: str):
    const = DBManager().list_all(db_name, collection)
    return const


@app.post("/topic/last")
async def save_topic(info: Request):
    data_json = await info.json()
    print(data_json)
    if data_json['topic'] is not None:
        return DBManager().save_last_topic(data_json['topic'], data_json)
    return DBManager().save_last_topic('none', data_json)

@app.get("/topic/last")
async def get_topic(topic: str = 'none'):
    if topic is 'none':
        return {'status': 'none'}
    return DBManager().get_last_topic(topic)

