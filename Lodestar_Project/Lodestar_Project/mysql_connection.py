import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="FAT_hippo88"
)

print(mydb)