import mysql.connector as Myconn

mydb=Myconn.connect(host="localhost",user="root",password="saim51214",database="wscube")
db_cursor=mydb.cursor()
db_cursor.execute("show tables")
for i in db_cursor:
    print(i)
