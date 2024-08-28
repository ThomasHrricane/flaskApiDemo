from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import text
app = Flask(__name__)

DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'wang2003'
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'DW'
app.config['SQLALCHEMY_DATABASE_URI'] \
    = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".\
    format(DIALECT,DRIVER,USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
db = SQLAlchemy(app)

# with app.app_context():
#     with db.engine.connect() as conn:
#         rs = conn.execute(text('select 1'))
#         print(rs.fetchone())

class User(db.Model):
    # 定义表名
    __tablename__ = 'users'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)

with app.app_context():
    db.create_all()


# @app.route('/')
# def index():
#     return render_template('test.html')

# @app.route('/user/add')
# def user_add():
#     user1 = User(username = '张三', password = '111111')
#     user2 = User(username = '李四', password = '222222')
#     user3 = User(username = '王五', password = '333333')
#     db.session.add(user1)
#     db.session.add(user2)
#     db.session.add(user3)
#     db.session.commit()
#     return '用户已创建成功'

@app.route('/')
def user_query():
    users = User.query.all()
    # json返回
    user_list = []
    for user in users:
        content = {'username': user.username, 'password': user.password}
        user_list.append(content)
    return jsonify(user_list)
    # 列表返回
    # return render_template('query.html', users = users)

if __name__ == '__main__':
    app.run()
