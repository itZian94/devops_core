from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import requests
from os import getenv

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://root:root@35.246.43.74/prize_generator'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

db.drop_all()

class Keyword(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column('value', db.String(99), nullable=False)

db.create_all()

@app.route('/', methods=['GET'])
def homepage():
    keyword = ""
    service2_response = requests.get("http://service2:5501/randint").text
    service3_response = requests.get("http://service3:5502/randalpha").text
    #value = str(service2_response) + str(service3_response)
    value = service3_response + service2_response
    keyword = Keyword(value=value)
    db.session.add(keyword)
    db.session.commit()
    keywords=Keyword.query.first()
    return render_template("home.html", keyword=keyword)

@app.route('/result', methods=['GET'])
def result():
    complete = ""
    service4_response = requests.get("http://service4:5503/complete").text
    complete = service4_response
    return render_template("result.html", complete=complete)


if __name__=='__main__':
  app.run(host='0.0.0.0', port=5500, debug=True)