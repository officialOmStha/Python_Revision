import sqlite3 

con = sqlite3.connect("Practice.db")

cursor = con.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS college(
    id INTEGER,
    name TEXT,
    address TEXE,
    streme TEXT,
    location TEXT
    )
    """
)


records = [
    (1, "ABC", "KTM", "BIM", "Baneshwor"),
    (2, "XYZ", "LTP", "BCA", "Jawalakhel")]

# cursor.executemany(
#     "INSERT INTO college VALUES(?,?,?,?,?)", records
# )

# con.commit()

cursor.execute("SELECT * FROM college")

for i in cursor.fetchall():
    print(i)

cursor.execute("""UPDATE college SET location='Melamchi'  WHERE id=1""")

con.commit()

cursor.execute("SELECT * FROM college")

for i in cursor.fetchall():
    print(i)