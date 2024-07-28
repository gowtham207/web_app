import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
SECRET_SALT = os.getenv('SECRET_SALT')
SECRET_KEY = os.getenv('SECRET_KEY')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
EFS_ROOT = os.getenv('EFS_ROOT')

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def db_con():
    con = None
    cur = None
    try:
        con = mysql.connector.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            port=DB_PORT
        )
        if con.is_connected():
            db_info = con.get_server_info()
            logger.info("Connected to MySQL Server version %s", db_info)
            cur = con.cursor(dictionary=True)  # Use dictionary=True for dict-like cursor
            logger.info('Database connection established successfully.')
            return con, cur
    except Error as e:
        logger.error(f"MySQL Error: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
    return con, cur
