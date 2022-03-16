from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer, String

db_uri = 'postgres://postgresql+:postgres@192.168.56.107:5432'
engine = create_engine(db_uri)

# Create a metadata instance
metadata = MetaData(engine)
# Declare a table
table = Table('Example',metadata,
              Column('id',Integer, primary_key=True),
              Column('name',String))
# Create all tables
metadata.create_all()
for _t in metadata.tables:
   print("Table: ", _t)
