import os
from dotenv import load_dotenv

class ConfigLoader:
    def __init__(self):
        load_dotenv()
        self._load_config()

    def _load_config(self):
        self.mongodb_uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017/botopia_db")
        self.port = int(os.getenv("PORT", "8000"))
        self.app_env = os.getenv("APP_ENV", "development")

    def get_mongodb_uri(self):
        return self.mongodb_uri

    def get_port(self):
        return self.port

    def get_app_env(self):
        return self.app_env
