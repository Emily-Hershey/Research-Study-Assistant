from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_twisted import Twisted

app = Flask(__name__)
CORS(app)
twisted = Twisted(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/hersh/Practice-Questions-Bot-1/app/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)





