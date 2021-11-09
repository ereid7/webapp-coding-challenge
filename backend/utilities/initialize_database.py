import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import postgresconfig

def create_database():
  # Connect to PostgreSQL DBMS
  con = psycopg2.connect(f"user={postgresconfig.user} password={postgresconfig.password} port={postgresconfig.port}")
  con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

  # Obtain a DB Cursor
  cursor = con.cursor()
  name_Database = "PruductInfo"

  # Create table statement
  sqlCreateDatabase = "create database "+name_Database+";"

  # Create a table in PostgreSQL database
  cursor.execute(sqlCreateDatabase)

def create_tables():
  """ create tables in the PostgreSQL database"""
  commands = (
    """
    CREATE TABLE product (
       product_id serial PRIMARY KEY
     , product_name text UNIQUE
    )""",
    """
    CREATE TABLE ingredient (
       ingredient_id serial PRIMARY KEY
     , ingredient_name text UNIQUE
    )""",
    """
    CREATE TABLE product_ingredient (
       product_id    int REFERENCES product (product_id) ON UPDATE CASCADE ON DELETE CASCADE
     , ingredient_id int REFERENCES ingredient (ingredient_id) ON UPDATE CASCADE
     , PRIMARY KEY (product_id, ingredient_id)
    )
    """)

  conn = None
  try:
    # read the connection parameters
    params = f"dbname=pruductinfo user=postgres password='admin' port={postgresconfig.port}"
    # connect to the PostgreSQL server
    conn = psycopg2.connect(params)
    cur = conn.cursor()
    # create table one by one
    for command in commands:
        cur.execute(command)
    # close communication with the PostgreSQL database server
    cur.close()
    # commit the changes
    conn.commit()
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  finally:
    if conn is not None:
      conn.close()

if __name__ == '__main__':
  create_database()
  create_tables()