import sqlite3
import time

start = time.time()
conn = sqlite3.connect('example.db')
conn.row_factory = sqlite3.Row
conn.execute('''PRAGMA synchronous=off;''')
conn.execute('''PRAGMA journal_mode=wal;''')

conn.execute('''create table if not exists sample (id int, name text, detail text, update_time text)''')

i = 0
for i in range(20000000):
    conn.execute("insert or replace into sample values (:id, 'test', 'testseteste', datetime(CURRENT_TIMESTAMP, 'localtime'))", {"id":i})

conn.commit()
print(time.time() - start)
