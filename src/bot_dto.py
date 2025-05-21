from pydantic import BaseModel
from typing import List, Optional, Dict
from datetime import datetime
from bson import ObjectId


class BotProfile(BaseModel):
    id: str
    name: str
    bot_name: str
    description: str
    purpose: str
    visibility: str
    user_id: str
    company_id: str
    created_at: datetime
    updated_at: datetime


class PersonalityInstructions(BaseModel):
    base_prompt: str
    behavior_description: str
    traits: List[str]


class PersonalityBehaviors(BaseModel):
    argumentative: float
    factual: float
    correctness: float
    sarcasm: float
    rudeness: float
    politeness: float
    empathy: float
    creativity: float
    spontaneity: float
    organization: float


class Personality(BaseModel):
    tone: str
    style: str
    example_phrases: List[str]
    instructions: PersonalityInstructions
    behaviors: PersonalityBehaviors
    skip_quotient: float


class ResponseSettings(BaseModel):
    response_format: str
    fallback_message: str


class ExternalIntegrations(BaseModel):
    google_drive_enabled: bool
    notion_enabled: bool
    slack_enabled: bool


class DataSources(BaseModel):
    upload_files: List[str]
    pasted_text_blocks: List[str]
    web_urls: List[str]
    external_integrations: ExternalIntegrations


class RagSettings(BaseModel):
    use_vector_store: bool
    vector_store_type: str
    restrict_answers_to_data: bool
    allow_fallback_to_llm: bool


class MemorySettings(BaseModel):
    allow_memory: bool
    memory_type: str
    max_memory_length: int


class ToolsEnabled(BaseModel):
    web_search: bool
    code_execution: bool
    custom_apis: List[str]


class GetBotDTO(BaseModel):
    id: str
    bot_profile: BotProfile
    personality: Personality
    response_settings: ResponseSettings
    data_sources: DataSources
    rag_settings: RagSettings
    memory_settings: MemorySettings
    tools_enabled: ToolsEnabled

    class Config:
        json_encoders = {
            ObjectId: str
        }

class CreateBotDTO(BaseModel):
    bot_profile: BotProfile
    personality: Personality
    response_settings: ResponseSettings
    data_sources: DataSources
    rag_settings: RagSettings
    memory_settings: MemorySettings
    tools_enabled: ToolsEnabled