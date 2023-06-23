from dotenv import load_dotenv
import os

DEBUG = True

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
SERVER = os.getenv('SERVER')
DB = os.getenv('DB')
PORT = os.getenv('PORT')
SECRET_KEY = os.getenv('SECRET_KEY')

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True
