import sqlite3
import pandas as pd

conn = sqlite3.connect(host="localhost", user="root", passwd="root", database="burakku_jakku")

cursor = conn.cursor()

data_sql_1 = pd.read_sql("SELECT * FROM jugador", conn)

print(data_sql_1.head())