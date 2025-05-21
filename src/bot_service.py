from src.bot_dto import CreateBotDTO, GetBotDTO
from src.bot_repository import BotRepository
from typing import List


class BotService:
    def __init__(self, bot_repository: BotRepository):
        self.bot_repository = bot_repository

    def create_bot(self, bot_data: CreateBotDTO):
        return self.bot_repository.save_bot(bot_data)

    def get_bots_by_user(self, user_id: str) -> List[GetBotDTO]:
        return self.bot_repository.get_bots_by_user(user_id)