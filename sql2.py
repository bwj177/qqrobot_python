import sqlite3

conn = sqlite3.connect('bot.db')

print("数据库打开成功")

c = conn.cursor()
c.execute('''CREATE TABLE score
       (id INTEGER PRIMARY KEY AUTOINCREMENT,
       QQ           INT    NOT NULL,
       Score        int    default 0,
       group_id         CHAR(500),
       SALARY         REAL);''')

print("数据表创建成功")
conn.commit()
conn.close()