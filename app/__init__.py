from flask import Flask
from flask_pymongo import PyMongo
import os

app = Flask(__name__)

#
app.config["MONGO_URI"] = 'mongodb://trupti_samant:Ishaadi02@ds257314.mlab.com:57314/neuralchefs'
# app.config["MONGO_URI"] = 'mongodb://joe_reynolds:op3nupd4n@ds155903.mlab.com:55903/heroku_j29mjxk2'
# Set base directory ##################################################
app.config['basedir'] = os.path.abspath(os.path.dirname(__file__))


# store the PyMongo/MongoDBB client object in the flask app.config
app.config['pymongo_db'] = PyMongo(app)

from app import routes, models, recipes, config, mongodb
# import app
#
app.run(debug=True)
# mongodb.insert_recipe()
