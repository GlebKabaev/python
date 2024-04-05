import sqlite3
with sqlite3.connect('database.db') as db:
    cursor=db.cursor()
    queryCreate = """ CREATE TABLE IF NOT EXISTS doctor(id INTEGER PRIMARY KEY,name TEXT,major TEXT)  """
    query1="""INSERT INTO doctor (id,name,major) VALUES(1,'Бутько Игорь Морелономиконович','Хирург') """
    query2="""INSERT INTO doctor (id,name,major) VALUES(2,'Жмыхченко Михаил Петрович','Невролог') """
    query3 = """INSERT INTO doctor (id,name,major) VALUES(3,'Патапенко Василий Демидович','Травмотолог') """
    queryCreate2 = """ CREATE TABLE IF NOT EXISTS ward (id INTEGER PRIMARY KEY,quantity INTEGER)"""
    queryCreate3 = """ CREATE TABLE IF NOT EXISTS patient(id INTEGER PRIMARY KEY,name TEXT,id_ward INTEGER,id_doc INTEGER,FOREIGN KEY (id_ward) REFERENCES ward (id),FOREIGN KEY (id_doc) REFERENCES doctor (id))  """
    query4= """INSERT INTO ward (id,quantity) VALUES(1,5) """
    query5 = """INSERT INTO ward (id,quantity) VALUES(2,4) """
    query6 = """INSERT INTO ward (id,quantity) VALUES(3,3) """
    query7="""INSERT INTO patient (id,name,id_ward,id_doc) VALUES(1,'Лобинсов Григорий Альбертович',1,1) """
    query8 = """INSERT INTO patient (id,name,id_ward,id_doc) VALUES(2,'Лобинсов Тарок Альбертович',1,2) """
    query9 = """INSERT INTO patient (id,name,id_ward,id_doc) VALUES(3,'Лобинсов Барок Альбертович',2,2) """
    querySelect="""SELECT * FROM patient"""
    cursor.execute(querySelect)
    print(cursor.fetchall())
    querySelect="""SELECT * FROM ward"""
    cursor.execute(querySelect)
    print(cursor.fetchall())
    querySelect="""SELECT * FROM doctor"""
    cursor.execute(querySelect)
    print(cursor.fetchall())

