import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SECRET_KEY= os.getenv("SECRET_KEY", "change-me")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # where logs will be written (app creates this on startup if needed)
    LOG_DIR = os.path.join(os.path.dirname(__file__), 'logs')
    