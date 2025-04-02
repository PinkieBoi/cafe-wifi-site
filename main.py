import os
from random import choice
from dotenv import load_dotenv
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Boolean
from flask import Flask, jsonify, render_template, request
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

load_dotenv(".env")

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
Bootstrap(app)

# Create DB
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["SQLALCHEMY_DATABASE_URI"]
db = SQLAlchemy(model_class=Base)
db.init_app(app)


@app.route("/")
def home():
    return render_template('index.html')




if __name__ == "__main__":
    app.run(debug=True, port=3000)