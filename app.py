from flask import Flask

# flaskのインタスタンスを作成
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# dbの設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)


# モデルの定義
class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)


@app.route('/')
def index():
	# Topページ(index.html)を表示する
	return 'Hello, World'


if __name__ == '__main__':
	app.run(debug=True)
