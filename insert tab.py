import mysql.connector as Myconn

mydb=Myconn.connect(host="localhost",user="root",password="saim51214",database="wscube")
db_cursor=mydb.cursor()
db_cursor.execute("insert into student(id,name,email,age,status) values(%s,%s,%s,%s,%s)",(5,"zain","@zangmail.com",22,3))
mydb.commit()
print(db_cursor.rowcount,"Record inserted")


#its change some specific data at line 5 ending part
