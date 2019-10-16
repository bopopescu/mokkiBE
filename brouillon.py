from connectDB import connection

mycursor = connection.cursor()

sql = "SELECT * FROM Users WHERE first_name ='Bruce'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

getemails = "SELECT company_email from Users"

mycursor = connection.cursor()
mycursor.execute(getemails)
allemails = mycursor.fetchall()
mycursor.close()

teteo=type(allemails)

print(teteo)

print(allemails)

def checkemail(email,allemails):
    if email in allemails :
        return True
    return False

checkemail(('bruce@lee.china',),allemails)

insert_stmt = (
     "INSERT INTO employees (emp_no, first_name, last_name, hire_date) "
     "VALUES (%s, %s, %s, %s)"
 )
data = (2, 'Jane', 'Doe', datetime.date(2012, 3, 23))
cursor.execute(insert_stmt, data)

select_stmt = "SELECT * FROM Users WHERE first_name = %(first_name)s"

firstName='Bruce'

mycursor.execute(select_stmt, { 'first_name': firstName })

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

name='Bruce'
cursor = connection.cursor()
select_stmt = "SELECT * from Users WHERE first_name = %(first_name)s"
cursor.execute(select_stmt, { 'first_name': name })
data = cursor.fetchall()
connection.commit()
cursor.close()

print(data)

name="bruce"
mycursor = connection.cursor()
select_stmt= "SELECT * from Users WHERE first_name = %s"
mycursor.execute(select_stmt,name)
data = mycursor.fetchall()
connection.commit()
mycursor.close()


