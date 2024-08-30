import mysql.connector as my

con=my.connect(
    host="localhost",
    user="root",
    password="12345@As",
    database="ecommerce"  
)

cr = con.cursor()

cr.execute("use ecommerce")
# cr.execute("create table products(id int, name varchar(50),city varchar(50))")



cr.execute("insert into products(id,name,city) values(2,'piyush','gkp')")
con.commit()
cr.close()



