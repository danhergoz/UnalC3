import mysql.connector

mydb = mysql.connector.connect(
  host="153.92.215.93",
  user="frnimoaq_mintic",
  passwd="unal@2021",
  database="frnimoaq_nomina"
)

mycursor = mydb.cursor()

consulta = "SELECT ciuo_ocupacion FROM ciuo"
mycursor.execute(consulta)
myresult = mycursor.fetchall()
print(type(myresult))
print(myresult)
