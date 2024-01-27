import mysql.connector
#maybe this commit will fix it?


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="FAT_hippo88"
)

print(mydb)