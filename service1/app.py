from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@35.246.43.74/prize_generator'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

db.drop_all()
db.create_all()

class Key(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column('value', db.String(11), nullable=False)

@app.route('/', methods=['GET'])
def homepage():
    keys = ""
    service2_response = requests.get("http://service2:5501/randint")
    service3_response = requests.get("http://service3:5502/randalpha")
    alpha = str(service2_response)
    value = alpha+service3_response
    key = Key(value=value)
    db.session.add(result)
    db.session.commit()
    return render_template("home.html", keys=keys)

@app.route('/result', methods=['GET'])
def result():
    results = ""
    return render_template("result.html", results=results)


if __name__=='__main__':
  app.run(host='0.0.0.0', port=5500, debug=True)