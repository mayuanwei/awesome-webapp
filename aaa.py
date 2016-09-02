import mysql.connector


conn = mysql.connector.connect(user='root',password='123',db='test')
'''pool = aiomysql.create_pool(
    host='localhost',
    port=3306,
    user='root',
    password='123',
    db='test',
    charset='utf8',
    autocommit=True,
    maxsize=10,
    minsize=1,
)

conn = pool
cur = conn.cursor(aiomysql.DictCursor)'''
cur = conn.cursor()

sql = '''select * from USER WHERE id = %s
'''
cur.execute(sql % '3')
res = cur.fetchall()
print(res)
