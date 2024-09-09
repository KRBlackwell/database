import sys
import configparser
import psycopg2 as pg
import os

config = configparser.ConfigParser()
config_file = os.path.join(os.environ['HOME'], 'db_config.ini')
config.read(config_file)

USER = config.get('credentials', 'user')
PASSWORD = config.get('credentials', 'password')
NEW_PASSWORD = config.get('credentials', 'newpassword')
HOST = config.get('credentials', 'host')
DBNAME = config.get('credentials', 'dbname')

pg_connection_dict = {
    'dbname': DBNAME,
    'user': USER,
    'password': PASSWORD,
    'host': HOST
}

try:
  conn = pg.connect(**pg_connection_dict)
  print("connected")
except Exception as e:
  print("couldn't connect", e)

cur = conn.cursor()
ddl_stmt = """alter user %(user) with password %(password)s"""
cur.execute(ddl_stmt, {"user": USER, "password": NEW_PASSWORD})
print("changed password")

print("close connection and redo with new password to check")
try:
  cur.close()
  conn.close()
except Exception as e:
  print("couldn't close:", e)

pg_connection_dict = {
    'dbname': DBNAME,
    'user': USER,
    'password': NEW_PASSWORD,
    'host': HOST
}
try:
  conn = pg.connect(**pg_connection_dict)
  print("connected")
except Exception as e:
  print("couldn't connect", e)
print("connected. get some table info to test:")
cur.execute("""select table_name from information_schema.tables order by table_name limit 5;""")
results = cur.fetchall()
for row in results:
  print(row)

try:
  cur.close()
  conn.close()
except Exception as e:
  print("couldn't close:", e)
