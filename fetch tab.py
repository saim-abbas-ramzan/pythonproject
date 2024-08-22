import mysql.connector as Myconn

mydb=Myconn.connect(host="localhost",user="root",password="saim51214",database="wscube")
db_cursor=mydb.cursor()

db_cursor.execute("select * from wscube.student")
db_select=db_cursor.fetchall()
print(db_select)

#line 7 replace with -> db_select=db_cursor.fetchone()
# it meand show only one person data