import sqlite3
import time

start = time.time()
conn = sqlite3.connect('example.db')

c = conn.cursor()

c.execute('''create table if not exists sample (id int, name text, detail text)''')

i = 0
for i in range(20000000):
    c.execute("insert into sample values (?, 'test', 'testseteste')", (i,))

conn.commit()
print(time.time() - start)
