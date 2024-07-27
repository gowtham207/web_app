import psycopg2
from psycopg2.extras import RealDictCursor


def db_con():
    con = psycopg2.connect(user="postgres", password='toor',
                           dbname="backend", host="localhost")
    return con, con.cursor(cursor_factory=RealDictCursor)
