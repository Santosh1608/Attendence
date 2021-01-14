import psycopg2
import psycopg2.extras


def connection():
    conn = psycopg2.connect(dbname='testdb',
                            user='postgres',
                            host='localhost',
                            password='san123',
                            )
    c = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    return c, conn
