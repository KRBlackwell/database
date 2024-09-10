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

def do_query(query):
  cursor.execute(query)
  rows = cursor.fetchall()
  print()
  print()
  print("executed sql query:", query)
  try:
    for row in rows:
      print(row)
  except Exception as e:
    print(e)

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

#this is a good query
#query = """SELECT table_name
#           FROM (SELECT table_name
#                 FROM all_tables
#                 ORDER BY table_name)
#          WHERE ROWNUM <= 5"""

query1 = """SELECT * FROM ALL_TAB_COLUMNS WHERE OWNER='EXAMPLE'"""
query2 = """SELECT * FROM ALL_TAB_COLUMNS WHERE table_name = 'PERSON_DEMO'"""
query3 = """SELECT * FROM all_tables where table_name = 'PERSON_DEMO'"""

do_query(query1)
do_query(query2)
do_query(query3)

cursor.close()
connection.close()
