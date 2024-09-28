from importlib import metadata
import pandas as pd
from sqlalchemy import MetaData, create_engine
from constants import db_path

engine = create_engine('sqlite:///./data/traffic_pd.db')

csv_file =  'data/Liczniki - dzienne.csv'
df = pd.read_csv(csv_file, encoding='utf-8', on_bad_lines='skip')
print(df)

df.to_sql('traffic_pd', con=engine, if_exists='replace', index=False)

