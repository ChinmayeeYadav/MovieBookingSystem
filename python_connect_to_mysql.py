import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='Chinmay33@9',database='dbms_mini_project')
my_cursor=conn.cursor()
conn.commit()
conn.close()
print("Connection Successfully Created")