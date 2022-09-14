import json

from fastapi import FastAPI, Request

from src.database.db_manager import DBManager

app = FastAPI()
db = DBManager()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/store/{db_name}/{collection}")
async def list_all(db_name: str, collection: str):
    const = db.list_all(db_name, collection)
    return const


@app.post("/store/{db_name}/{collection}")
async def insert(db_name: str, collection: str, info: Request):
    dataJson = await info.json()
    const = db.insert(db_name, collection, dataJson)
    return const

@app.post("/topic/last")
async def save_topic(info: Request):
    data_json = await info.json()
    print(data_json)
    if data_json['topic'] is not None:
        return DBManager().save_last_topic(data_json['topic'], data_json)
    return db.save_last_topic('none', data_json)


@app.post("/generic/item")
async def save_item(info: Request):
    data_json = await info.json()
    return db.store_item(data_json)


@app.put("/generic/item/{uuid}")
async def save_item(uuid: str, info: Request):
    data_json = await info.json()
    return db.update_item(uuid, data_json)


@app.get("/generic/item/{uuid}")
async def get_item(uuid: str):
    return db.get_item(uuid)


@app.get("/topic/last")
async def get_topic(topic: str = 'none'):
    if topic == 'none':
        return {'status': 'none'}
    return db.get_last_topic(topic)


