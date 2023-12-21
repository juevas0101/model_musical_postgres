from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv
from .models import db
from .routes.client_route import client_blueprint
import os

load_dotenv()

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(client_blueprint)

migrate = Migrate(app, db, directory='src/data')

if __name__ == '__main__':
    app.run(debug=True)

