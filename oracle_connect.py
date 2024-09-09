import os
import configparser
import getpass
import oracledb

config = configparser.ConfigParser()
config_file = os.path.join(os.environ['HOME'], 'db_config.ini')
config.read(config_file)

user = config.get('credentials', 'user')
pw = config.get('credentials', 'oracle_password')
dsn = config.get('credentials', 'oracle_dsn')

#this is None on Linux:
instant_client_dir = None

oracledb.init_oracle_client(lib_dir=instant_client_dir)
print("oracledb client version:", oracledb.clientversion())
if pw is None:
  pw = getpass.getpass("Enter password for %s:" % user)

try:
  connection = oracledb.connect(
    user=user,
    password=pw,
    dsn=dsn
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
