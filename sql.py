import sqlite3

with sqlite3.connect("blog.db") as conn:


  values=[("Good", "I\'m good."),
          ("Well","I\'m well."),
          ("Excellent","I\'m Excellent."),
          ("Okay","I\'m Okay.")]



  cursor=conn.cursor()

  cursor.execute("""CREATE TABLE posts
                (title TEXT, post TEXT);""")


  cursor.executemany("""INSERT INTO posts VALUES(?,?)""",values)