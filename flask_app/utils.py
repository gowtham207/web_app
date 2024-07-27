import os
import psycopg2
from psycopg2.extras import RealDictCursor
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
        con = psycopg2.connect(
            user=DB_USER,
            password=DB_PASS,
            dbname=DB_NAME,
            host=DB_HOST,
            port=DB_PORT
        )
        cur = con.cursor(cursor_factory=RealDictCursor)
        logger.info('Database connection established successfully.')
        return con, cur
    except psycopg2.OperationalError as e:
        logger.error(f"OperationalError: {e}")
    except psycopg2.InterfaceError as e:
        logger.error(f"InterfaceError: {e}")
    except psycopg2.DatabaseError as e:
        logger.error(f"DatabaseError: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
