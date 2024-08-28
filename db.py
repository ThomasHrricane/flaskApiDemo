# import pymysql


# # 打开数据库连接
# try:
#     db = pymysql.connect(host='localhost', user='root', passwd='123456', port=3306)
#     print('连接成功！')
# except:
#     print('something wrong!')

# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()


# # sql = "CREATE DATABASE IF NOT EXISTS EcomDW"#new_db是要创建的数据库名字

# # # 执行创建数据库的sql语句
# # cursor.execute(sql)
# cursor.execute('USE EcomDW')

# # 使用 execute()  方法执行 SQL 查询
# # sql1 = """CREATE TABLE base_attr_value (
# #          id  CHAR(20) NOT NULL,
# #          value_name  CHAR(20),
# #          attr_id CHAR(20)  NOT NULL
# #            )"""

# # sql2 = """CREATE TABLE base_attr_info (
# #          id  CHAR(20) NOT NULL,
# #          attr_name  CHAR(20),
# #          category_id CHAR(20)  NOT NULL,
# #          category_level CHAR(20)
# #            )"""

# # cursor.execute(sql1)
# # cursor.execute(sql2)
# # print('建表成功！')


# # 使用 fetchone() 方法获取单条数据.
# # data = cursor.fetchone()

# # print("Database version : %s " % data)



# try:
#     cursor.execute("select * from user order by userID desc")
#     users = cursor.fetchall()
#     print("数据表user的数据列表")
#     print("")
#     for user in users:
#         print(str(user[0]) + "@" + user[7])
#     print("")
# except Exception as e:
#     print(e)





# db.close()






from sqlalchemy import create_engine
from sqlalchemy.sql import text



HOSTNAME = '127.0.0.1'
DATABASE = 'EcomDW'
PORT = 3306
USERNAME = 'root'
PASSWORD = '123456'
DB_URL = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
engine = create_engine(DB_URL)


with engine.connect() as conn:
    # 执行原生SQL语句
    print("CHOEUOWC")
    results = conn.execute(text("SELECT * FROM baseattrinfo"))
    # 遍历所有数据
    for result in results:
        print(result)


