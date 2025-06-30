import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import random


# Database connection details

import pandas as pd

'''di={"current_artist":[],"first_recommendation":[],"second_recommendation":[],"third_recommendation":[]}
df=pd.DataFrame(pd.read_csv("data2.csv"))
#print(df[:5:])
rf=df["artist"].unique()
print(len(rf))
for x in rf :
    di["current_artist"].append(x)
    di["first_recommendation"].append(random.choice(rf))
    di["second_recommendation"].append(random.choice(rf))
    di["third_recommendation"].append(random.choice(rf))
dt=pd.DataFrame(di,columns=["current_artist","first_recommendation","second_recommendation","third_recommendation"])
#print(di)
print(dt.columns)'''
#user = 'root'
#passw = '2004'
#host = '127.0.0.1'
#port = 3306
#database = 'auth_system'

#engine = create_engine(f'mysql+pymysql://{user}:{passw}@{host}:{port}/{database}')

#tor.to_sql(name='recommend', con=engine, if_exists='append', index=False)

#engine.dispose()

#print("Data inserted successfully!")

'''
user = 'root'
passw = '2004'
host = '127.0.0.1'
port = 3306
database = 'auth_system'

# Create SQLAlchemy engine for MySQL
engine = create_engine(f'mysql+pymysql://{user}:{passw}@{host}:{port}/{database}')

# Insert the DataFrame into MySQL database using to_sql method
dt.to_sql(name='recommend_artist', con=engine, if_exists='append', index=False)

# Closing the connection
engine.dispose()

print("Data inserted successfully!")'''

df=pd.DataFrame(pd.read_csv("data2.csv"))
max =None
for x in df["artist"]:
    if max is None or max<len(x):
        max=len(x)
print(max)

