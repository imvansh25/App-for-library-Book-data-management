import  sqlite3

def connect():
    con = sqlite3.connect("Book.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(ID INTEGER PRIMARY KEY, title TEXT , author TEXT, year INTEGER , ISBN INTEGER)")
    con.commit()
    con.close()

def insert(title,author,year,ISBN):
    con = sqlite3.connect("Book.db")
    cur = con.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,ISBN))
    con.commit()
    con.close()

def view_all():
    con = sqlite3.connect("Book.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM book")
    row = cur.fetchall()
    con.close()
    return row

def search(title,author,year,ISBN):
    con = sqlite3.connect("Book.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM book WHERE title=? or author=? or year=? or ISBN=?",(title,author,year,ISBN))
    row = cur.fetchall()
    con.close()
    return row

def delete(id):
    con = sqlite3.connect("Book.db")
    cur = con.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    con.commit()
    con.close()

def update(id,title,author,year,ISBN):
    con = sqlite3.connect("Book.db")
    cur = con.cursor()
    cur.execute("UPDATE book SET title=? , author=? , year=? , ISBN=? WHERE id=?",(title,author,year,ISBN,id))
    con.commit()
    con.close()

connect()
