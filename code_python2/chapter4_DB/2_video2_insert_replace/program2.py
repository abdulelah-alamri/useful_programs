import sqlite3

conn = sqlite3.connect("example.db")

c = conn.cursor()

c.execute('''CREATE IF NOT EXISTS TABLE Students 
          (Name TEXT, Id INTEGER PRIMARY KEY, AGE INTEGER, Grade REAL )''')

c.execute(''' INSERT INTO Students ('NAME', 'Id','AGE','Grade')
VALUES ('AHMED',2233,20,91.5)
''')

 

conn.commit()

conn.close()