from flask import Flask , request ,jsonify
from flask_sqlalchemy import SQLAlchemy
import os 

app = Flask(__name__)
# check for environment variable
# if not os.getenv("DATABASE_URL"):
#     raise RuntimeError("DATABASE_URL is not set"
# Define the database credentials
user = 'akash'
password = 'raj'
host = '127.0.0.1'
port = 3306
database = 'NameList'

dburi = "mysql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database)
app.config['SQLALCHEMY_DATABASE_URI'] = dburi#'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
db = SQLAlchemy(app)



class User(db.Model):
    __tablename__ = 'NameList'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(80), unique=True, nullable=False)
    lastName= db.Column(db.String(120), unique=True, nullable=False)

    # def __repr__(self):
    #     return '<User %r>' % self.firstName


#Read for db
def readDb():
  try:
    namelist = User.query.all()
    user = {}
    count = 1
    for name in namelist:
      print(name.firstName)
      key = "userName"+str(count)
      user[key] = {"firstName" : name.firstName,"lastName":name.lastName}
      count+=1
    return user
  except Exception as e:
        # e holds description of the error
        error_text = {"error": str(e)}
        return error_text


@app.route('/')
def hello():
    data = readDb()
    return(jsonify(data))

if __name__ == "__main__":
    
    app.run(host='0.0.0.0', port=5000)