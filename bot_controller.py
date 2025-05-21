from fastapi import APIRouter
from bot_dto import CreateBotDTO
from bot_service import BotService
from mongo_config import MongoDBConfig
from bot_repository import BotRepository

router = APIRouter()

# Setup dependencies
db_config = MongoDBConfig()
bot_repository = BotRepository(db_config)
bot_service = BotService(bot_repository)


@router.post("/bot")
def create_bot(bot_data: CreateBotDTO):
    result = bot_service.create_bot(bot_data)
    return {"message": "Bot created", "id": str(result.inserted_id)}

@router.get("/bot/{user_id}")
def get_bots_by_user(user_id: str):
    bots = bot_service.get_bots_by_user(user_id)
    return bots