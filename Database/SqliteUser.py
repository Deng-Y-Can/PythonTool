import sqlite3

# 连接到SQLite数据库
# 数据库文件是 test.db，如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# 创建一个表:
cursor.execute('CREATE TABLE IF NOT EXISTS user (id VARCHAR(20) PRIMARY KEY, name VARCHAR(20))')

# 插入一条记录:
cursor.execute("INSERT INTO user (id, name) VALUES ('7', 'Michael')")

# 查询一条记录:
cursor.execute('SELECT * FROM user WHERE id=?', ('1',))
values = cursor.fetchall()
print(values)

# 更新一条记录:
cursor.execute("UPDATE user SET name = 'Mike' WHERE id = '1'")

# 删除一条记录:
cursor.execute("DELETE FROM user WHERE id = '1'")

# 提交事务:
conn.commit()

# 关闭Cursor和Connection:
cursor.close()
conn.close()


print('创建数据库成功')