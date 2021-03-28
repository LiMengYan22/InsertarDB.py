import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="usuario",
  password="password",
  database="nombreDB"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Clientes (nombre, apellidos) VALUES (%s, %s)"
val = ("LI", "Meng Yan")
mycursor.execute(sql, val)

mydb.commit()

print("1 Cliente insertado, ID:", mycursor.lastrowid)
