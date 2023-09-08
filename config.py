import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env_example')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

TOKEN = os.getenv('TOKEN')
DATABASE_URL = os.getenv('DATABASE_URL')
