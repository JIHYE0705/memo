import datetime
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.dbStock


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/post', methods=['POST'])
def save_post():
    now = datetime.datetime.now()
    idx = 0
    title_receive = request.form['title_give']
    content_receive = request.form['content_give']
    reg_date = now.strftime('%Y-%m-%d %H:%M:%S')
    idx += 1


    doc = {
        'idx': idx,
        'title': title_receive,
        'content': content_receive,
        'reg_date': reg_date,

    }

    db.articles.insert_one(doc)

    return {"msg": "저장 완료"}


@app.route('/post', methods=['GET'])
def get_post():
    articles = list(db.article.find({}, {'_id':False}))
    return {'all_articles': articles}


@app.route('/post', methods=['DELETE'])
def delete_post():
    return {"result": "success"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)