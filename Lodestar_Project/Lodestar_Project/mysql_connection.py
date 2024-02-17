import mysql.connector
#maybe this commit will fix it?


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="FAT_hippo88"
)

print(mydb)

#not sure if file is relevant anymore as database had to be converted to SQL


#import pymysql

#conn = pymysql.connect(
    #host='localhost',
    #user='root',
    #password='mysql',
    #db='db',
    #charset='utf8mb4',
    #cursorclass=pymysql.cursors.DictCursor
#)