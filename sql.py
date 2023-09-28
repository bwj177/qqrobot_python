import sqlite3

conn = sqlite3.connect('bot.db')

print("数据库打开成功")

c = conn.cursor()
c.execute(
    "insert into score(QQ,score,group_id) values(?,?,?)",(646319630,100,596048079)
)

print("数据表创建成功")
conn.commit()
conn.close()