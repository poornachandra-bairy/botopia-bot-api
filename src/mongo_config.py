from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
import time
import logging
from retrying import retry
import traceback
from config import config_loader

class MongoDBConfig:
    def __init__(self):
        self.config_loader = config_loader.ConfigLoader()
        self.uri = self.config_loader.get_mongodb_uri()
        self._setup_logging()
        self._connect_to_db()
        self._setup_logging()
        self._connect_to_db()

    def _setup_logging(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    @retry(stop_max_attempt_number=3, wait_exponential_multiplier=1000, wait_exponential_max=10000)
    def _connect_to_db(self):
        try:
            self.logger.info("Attempting MongoDB connection with URI: %s", self.uri)
            self.client = MongoClient(
                self.uri,
                serverSelectionTimeoutMS=30000,
                socketTimeoutMS=30000,
                connectTimeoutMS=30000,
                maxPoolSize=50,
                waitQueueTimeoutMS=30000
            )
            self.db = self.client.get_database('botopia_db')
            self.logger.info("Successfully created MongoDB client")
            self._test_connection()
        except Exception as e:
            self.logger.error(f"MongoDB connection error: {str(e)}")
            self.logger.error(f"Connection URI: {self.uri}")
            self.logger.error(f"Full traceback: {traceback.format_exc()}")
            raise

    def _test_connection(self):
        try:
            self.client.admin.command('ping')
            self.logger.info("MongoDB Atlas connection successful.")
        except Exception as e:
            self.logger.error(f"MongoDB connection failed: {str(e)}")
            raise

    def get_db(self):
        return self.db