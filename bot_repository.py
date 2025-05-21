from bot_dto import CreateBotDTO, GetBotDTO
from mongo_config import MongoDBConfig
from typing import List

class BotRepository:
    def __init__(self, db_config: MongoDBConfig):
        self.db = db_config.get_db()
        self.collection = self.db['bots']  # Using 'bots' as the collection name

    def save_bot(self, bot_dto: CreateBotDTO):
        return self.collection.insert_one(bot_dto.dict())

    def get_bots_by_user(self, user_id: str) -> List[GetBotDTO]:
        bots = list(self.collection.find({"bot_profile.user_id": user_id}))
        return [GetBotDTO(**bot, id=str(bot["_id"])) for bot in bots]