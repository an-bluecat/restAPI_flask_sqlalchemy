from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import os
from sqlalchemy.ext.declarative import declarative_base
from flask_cors import CORS
# Base = declarative_base()

# class Myproduct1(Product, Base):
#     __tablename__ = 'product1'
  
# class Myproduct2(Product, Base):
#     __tablename__ = 'product2'




# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
#CORS
cors = CORS(app) #CORS every where, to specify origin, modify below
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}}) 

# Database
ENV = 'prod'
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/lexus'
else:
    app.debug = False
    # get it with: heroku config --app restapipostgre
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://bzsgdtmbfuwwwp:26d6e3d55f0b56c0efbf1a65176962e267d94a905c6ba4196ef5c6a438085096@ec2-34-197-188-147.compute-1.amazonaws.com:5432/d4ljc28eih0k69'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

# Product Class/Model
class ECE110(db.Model):
  __tablename__ = 'ECE110'
  id = db.Column(db.Integer, primary_key=True)
  israting = db.Column(db.Boolean)
  user = db.Column(db.String(100))
  comment = db.Column(db.String(2000))
  time = db.Column(db.String(50))
  likes = db.Column(db.Integer)
  rate = db.Column(db.Integer)


  def __init__(self, israting, user, comment, time, likes, rate):
    self.israting = israting
    self.user = user
    self.comment = comment
    self.time = time
    self.likes = likes
    self.rate = rate

class ECE297(db.Model):
  __tablename__ = 'ECE297'
  id = db.Column(db.Integer, primary_key=True)
  israting = db.Column(db.Boolean)
  user = db.Column(db.String(100))
  comment = db.Column(db.String(2000))
  time = db.Column(db.String(50))
  likes = db.Column(db.Integer)
  rate = db.Column(db.Integer)


  def __init__(self, israting, user, comment, time, likes, rate):
    self.israting = israting
    self.user = user
    self.comment = comment
    self.time = time
    self.likes = likes
    self.rate = rate

class ECE243(db.Model):
  __tablename__ = 'ECE243'
  id = db.Column(db.Integer, primary_key=True)
  israting = db.Column(db.Boolean)
  user = db.Column(db.String(100))
  comment = db.Column(db.String(2000))
  time = db.Column(db.String(50))
  likes = db.Column(db.Integer)
  rate = db.Column(db.Integer)


  def __init__(self, israting, user, comment, time, likes, rate):
    self.israting = israting
    self.user = user
    self.comment = comment
    self.time = time
    self.likes = likes
    self.rate = rate




# Product Schema
class ratingSchema(ma.Schema):
  class Meta:
    fields = ('id', 'israting', 'user', 'comment', 'time', 'likes', 'rate')

# Init schema
rating_schema = ratingSchema()
ratings_schema = ratingSchema(many=True)



def get_rating(argin):
  all_ratings = argin.query.all()
  result = ratings_schema.dump(all_ratings)
  return jsonify(result)

def add_rating(className):

  israting = request.json['israting']
  user = request.json['user']
  comment = request.json['comment']
  time = request.json['time']
  likes = request.json['likes']
  rate = request.json['rate']

  new_rating = className(israting, user, comment, time, likes, rate)

  db.session.add(new_rating)
  db.session.commit()

  return rating_schema.jsonify(new_rating)

def delete_rating(page, id):
  rating = page.query.get(id)
  db.session.delete(rating)
  db.session.commit()

  return rating_schema.jsonify(rating)

@app.route('/<page>',methods=['GET'])
def index(page):
    return get_rating(eval(page)) #page is a string, needs to convert to class

@app.route('/<page>', methods=['POST'])
def post(page):
    return add_rating(eval(page)) #page is a string, needs to convert to class

# Delete rating
@app.route('/<page>/<id>', methods=['DELETE'])
def delete(page,id):
    return delete_rating(eval(page), id)




# # Get All ratings
# @app.route('/rating', methods=['GET'])
# def get_ratings():
#   all_ratings = rating.query.all()
#   result = ratings_schema.dump(all_ratings)
#   return jsonify(result)

# # Get Single ratings
# @app.route('/rating/<id>', methods=['GET'])
# def get_rating(id):
#   rating = rating.query.get(id)
#   return rating_schema.jsonify(rating)

# # Update a rating
# @app.route('/rating/<id>', methods=['PUT'])
# def update_rating(id):
#   rating = rating.query.get(id)

#   name = request.json['name']
#   description = request.json['description']
#   price = request.json['price']
#   qty = request.json['qty']

#   rating.name = name
#   rating.description = description
#   rating.price = price
#   rating.qty = qty

#   db.session.commit()

#   return rating_schema.jsonify(rating)



# Run Server
if __name__ == '__main__':
  app.run()