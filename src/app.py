import pandas as pd

from utils import db_connect
engine = db_connect()

# your code here
engine
if engine:
    print("Conexión exitosa")

data = pd.read_csv('/workspaces/ML-Algorithm/data/raw/bank-marketing-campaign-data.csv')
data.to_sql('banck', engine, if_exists='replace', index=False)
 
