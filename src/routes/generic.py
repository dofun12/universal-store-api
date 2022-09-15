from fastapi import APIRouter, Request

from src.database.db_manager import DBManager

router = APIRouter()
db = DBManager()


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
