import sqlalchemy
from sqlalchemy import text, bindparam
from sqlalchemy.orm import Session
import time

start = time.time()
engine = sqlalchemy.create_engine('sqlite:///superdb.db', echo=True)

engine.execute('''create table if not exists sample (id int, name text, detail text)''')

session = Session(
        bind = engine,
        autocommit = False,
        autoflush = True
        )

i = 0
for i in range(10000):
    sql = text('''
            insert into sample values (:id, 'test', 'testseteste')
            ''', bindparams=[bindparam('id', i)])
    session.execute(sql)
#    session.execute("insert into sample values (?, 'test', 'testseteste')", )
session.commit()

engine.execute("drop table sample")

print(time.time() - start)


# 普通に sqlite3 を利用した方が早い
# https://www.366service.com/jp/qa/f822f7920933b029eb28c5d07fb2f5d9
