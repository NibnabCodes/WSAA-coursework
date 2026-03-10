# Inserts data into database table

import mysql.connector 
 
db = mysql.connector.connect( 
  host="localhost", 
  user="root", 
  password="", 
  database="wsaa" 
) 
 
cursor = db.cursor() 
sql="insert into student (name, age) values (%s,%s)" 
values = ("NibNab",30) 
 
cursor.execute(sql, values) 
 
db.commit() 
print("1 record inserted, ID:", cursor.lastrowid) 
cursor.close() 
db.close() 