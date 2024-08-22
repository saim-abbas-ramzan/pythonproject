import mysql.connector as Myconn

mydb=Myconn.connect(host="localhost",user="root",password="saim51214",database="wscube")
db_cursor=mydb.cursor()
db_deltedata="delete from wscube.student where id=%s"
db_value=(72,)
db_cursor.execute(db_deltedata,db_value)
mydb.commit()
print(db_cursor.rowcount,"Record deleted")

# when all data delete then line 6 skip and line  5 replace
# -> db_deltedata="truncate table wscube.student"
# line 7 replace -> db_cursor.execute(db_deltedata)