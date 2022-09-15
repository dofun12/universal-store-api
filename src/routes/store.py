from typing import Union

from fastapi import APIRouter, Request

from src.database.db_manager import DBManager

router = APIRouter()
db = DBManager()
GENERIC_STORE_DB = 'simple-store'


@router.get("/store/{collection}")
async def list_all(collection: str, filter_key: Union[str, None] = None, filter_value: Union[str, None] = None):
    if filter_key is not None and filter_value is not None:
        return db.list_all(GENERIC_STORE_DB, collection, {filter_key: filter_value})
    return db.list_all(GENERIC_STORE_DB, collection)


@router.post("/store/{collection}")
async def insert(collection: str, info: Request):
    data_json = await info.json()
    const = db.insert(GENERIC_STORE_DB, collection, data_json)
    return const
