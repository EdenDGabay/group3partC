import os
from dotenv import load_dotenv
load_dotenv()

# Secret key setting from .env for Flask sessions
SECRET_KEY = os.environ.get('SECRET_KEY')

# DB base configuration from .env for modularity and security reasons
DB = {
    'uri' : os.environ.get('DB_URI'),
    'database': os.environ.get('DB_NAME')
}
