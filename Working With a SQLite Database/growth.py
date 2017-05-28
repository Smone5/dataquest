import pandas as pd
import sqlite3
import math

conn = sqlite3.connect("factbook.db")

sql = "SELECT * FROM facts;"

df = pd.read_sql_query(sql,conn)
df.dropna()
df[df["area_land"] > 0]
df[df["area_water"] > 0]
df[df["migration_rate"] > 0]
df[df["population"] > 0]

def final_pop(row):
	growth = row['population_growth'] / 100
	N = row['population'] *(math.e**(growth * 35))
	return round(N,0)
    
df['future_pop'] = df.apply(final_pop, axis=1) 
print(df.head(30))
