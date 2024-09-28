# sqlalchemy database
# DEPRACATED
from importlib import metadata
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, Boolean
import os
import sys
# dir2_path: str = os.path.normpath(os.path.join(os.path.dirname(__file__), '../res'))
# sys.path.append(dir2_path)
import constants as res

metadata = MetaData()
engine=create_engine('sqlite:///'+res.db_path, echo=True)
table_traffic = Table('sentences', metadata,
              Column('index', Integer, primary_key=True),
              Column('ulica', String),
              Column('data', String),
              )

def create_database():
    metadata.create_all(engine)

def drop_database():
    metadata.drop_all(engine)

def insert_traffic(index, ulica, data):
    with engine.connect() as connection:
        connection.execute(table_traffic.insert().values(index=index, ulica=ulica, data=data))
        connection.commit()

def get_sentence(index):
    with engine.connect() as connection:
        result = connection.execute(table_traffic.select().where(table_traffic.columns.index == index))
        return result.fetchone()

def get_all_sentences():
    with engine.connect() as connection:
        result = connection.execute(table_traffic.select())
        return result.fetchall()

def get_last_index():
    with engine.connect() as connection:
        result = connection.execute(table_traffic.select().with_only_columns(table_traffic.columns.index).order_by(table_traffic.columns.index.desc()).limit(1))
        result = result.fetchone()
        if result is None:
            return 0
        return result[0]
    

def drop_sentence_by_index(index : int):
    with engine.connect() as connection:
        connection.execute(table_traffic.delete().where(table_traffic.columns.index == index))
        connection.commit()

# def insert_csv(file_path):
#     with open(file_path) as file:
#         lines = file.readlines()
#         for line in lines:
#             data= line.split(',')
#             for info in  data:


if __name__=='__main__':
    create_database()
    # insert_csv('/home/coolka/projects/python/dwa_kolka/malopolskie-dwa-kolka-server/data/Liczniki - dzienne.csv')