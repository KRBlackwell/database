import os
import configparser
import getpass
import oracledb

config = configparser.ConfigParser()
config_file = os.path.join(os.environ['HOME'], 'db_config.ini')
config.read(config_file)

USER = config.get('credentials', 'user')
PASSWORD = config.get('credentials', 'oracle_password')
DSN = config.get('credentials', 'oracle_dsn')

#this is None on Linux:
instant_client_dir = None

oracledb.init_oracle_client(lib_dir=instant_client_dir)
print("oracledb client version:", oracledb.clientversion())
if PASSWORD is None:
  PASSWORD = getpass.getpass("Enter password for %s:" % user)

try:
  connection = oracledb.connect(
    user=USER,
    password=PASSWORD,
    dsn=DSN
  )
except Exception as e:
  print("couldn't connect to db:", e) 
#need Exception handling, specify the exceptions

cursor = connection.cursor()
print("connection: got cursor")
query = """SELECT table_name
           FROM (SELECT table_name
                 FROM all_tables
                 ORDER BY table_name)
          WHERE ROWNUM <= 5"""
cursor.execute(query)
rows = cursor.fetchall()
print("executed query")
try:
  for row in rows:
    print(row)
except Exception as e: 
  print(e)
finally:
  cursor.close()
  connection.close()
