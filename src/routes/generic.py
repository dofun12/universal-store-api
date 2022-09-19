from fastapi import APIRouter, Request

from src.database.db_manager import DBManager

router = APIRouter()
db = DBManager()


@router.put("/generic/list/{uuid}")
async def append_list_item(uuid: str, info: Request):
    data_json = await info.json()
    return db.append_item(uuid, data_json)


@router.post("/generic/list")
async def add_list_item(info: Request):
    data = await info.body()
    if len(data) > 0:
        json_dict = await info.json()
        return db.store_list(json_dict)
    return db.store_list(None)


@router.post("/generic/item")
async def save_item(info: Request):
    data_json = await info.json()
    return db.store_item(data_json)


@router.patch("/generic/item/{uuid}")
async def save_item(uuid: str, info: Request):
    data_json = await info.json()
    return db.update_item(uuid, data_json)


@router.get("/generic/item/{uuid}")
async def get_item(uuid: str):
    return db.get_item(uuid)
