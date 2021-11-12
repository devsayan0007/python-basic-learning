import sqlite3
con = sqlite3.Connection("./database/sqlite3.db")
try:
    con.execute('''
               CREATE TABLE student (
                 st_id BIGINT AUTO_INCREMENT PRIMARY KEY,
                 st_name VARCHAR(50),
                 st_class VACHAR(10),
                 st_email VARCHAR(30)
               )
    ''')
    print("CREATE TABLE SUCCESSFULLY")
except:
     print("ERROR TO CREATE TABLE")