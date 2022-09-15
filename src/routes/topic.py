from src.database.db_manager import DBManager
from fastapi import Request, APIRouter

db = DBManager()
router = APIRouter()


@router.post("/topic/last")
async def save_topic(info: Request):
    data_json = await info.json()
    print(data_json)
    if data_json['topic'] is not None:
        return DBManager().save_last_topic(data_json['topic'], data_json)
    return db.save_last_topic('none', data_json)


@router.get("/topic/last")
async def get_topic(topic: str = 'none'):
    if topic == 'none':
        return {'status': 'none'}
    return db.get_last_topic(topic)
