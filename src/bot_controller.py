from fastapi import APIRouter, HTTPException, status
from fastapi.logger import logger
from src.bot_dto import CreateBotDTO
from src.bot_service import BotService
from src.mongo_config import MongoDBConfig
from src.bot_repository import BotRepository

router = APIRouter()

# Setup dependencies
db_config = MongoDBConfig()
bot_repository = BotRepository(db_config)
bot_service = BotService(bot_repository)


@router.post("/bot", response_model=dict)
def create_bot(bot_data: CreateBotDTO):
    try:
        result = bot_service.create_bot(bot_data)
        return {"message": "Bot created", "id": str(result.inserted_id)}
    except Exception as e:
        logger.error(f"Error creating bot: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create bot"
        )

@router.get("/bot/{user_id}", response_model=list)
def get_bots_by_user(user_id: str):
    try:
        bots = bot_service.get_bots_by_user(user_id)
        if not bots:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No bots found for this user"
            )
        return bots
    except Exception as e:
        logger.error(f"Error fetching bots: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch bots"
        )