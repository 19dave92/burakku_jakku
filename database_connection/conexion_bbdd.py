import mysql.connector as sql
import pandas as pd


conexion_bbdd = sql.connect(host="localhost", user="root", passwd="root", database="burakku_jakku")

cursor = conexion_bbdd.cursor()

consulta="select * from jugador"

#cursor.execute(consulta) # devuelve una lista de bases de datos disponibles en el servidor mysql

#print(cursor.fetchall())


df = pd.read_sql(consulta,conexion_bbdd)

print(df.head())


conexion_bbdd.close()
