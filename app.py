from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
ENV = 'dev'
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
class Product(db.Model):
  __tablename__ = 'product'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True)
  description = db.Column(db.String(200))
  price = db.Column(db.Float)
  qty = db.Column(db.Integer)

  def __init__(self, name, description, price, qty):
    self.name = name
    self.description = description
    self.price = price
    self.qty = qty

# Product Schema
class ProductSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'description', 'price', 'qty')

# Init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


# @app.route('/', methods=['GET'])
# def get():
#   return jsonify({"msg":"hello"})

# def my_func():
#     return jsonify({"msg":"hello"})


# routes = [
#     dict(route="/", func="index", page="index"),
#     dict(route="/about", func="about", page="about")
# ]

# for route in routes:
#     app.add_url_rule(
#         route["route"], #I believe this is the actual url
#         route["page"], # this is the name used for url_for (from the docs)
#     )
#     app.view_functions[route["page"]] = my_func()
def get_products1(argin):
  all_products = argin.query.all()
  result = products_schema.dump(all_products)
  return jsonify(result)

@app.route('/<page>')
def index(page):
  if page=='about':
     return get_products1(Product)
  elif page =="test":
     return jsonify({"msg":"test"})

# Create a Product

@app.route('/product', methods=['POST'])
def add_product():
  name = request.json['name']
  description = request.json['description']
  price = request.json['price']
  qty = request.json['qty']

  new_product = Product(name, description, price, qty)

  db.session.add(new_product)
  db.session.commit()

  return product_schema.jsonify(new_product)

# Get All Products
@app.route('/product', methods=['GET'])
def get_products():
  all_products = Product.query.all()
  result = products_schema.dump(all_products)
  return jsonify(result)

# Get Single Products
@app.route('/product/<id>', methods=['GET'])
def get_product(id):
  product = Product.query.get(id)
  return product_schema.jsonify(product)

# Update a Product
@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
  product = Product.query.get(id)

  name = request.json['name']
  description = request.json['description']
  price = request.json['price']
  qty = request.json['qty']

  product.name = name
  product.description = description
  product.price = price
  product.qty = qty

  db.session.commit()

  return product_schema.jsonify(product)

# Delete Product
@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
  product = Product.query.get(id)
  db.session.delete(product)
  db.session.commit()

  return product_schema.jsonify(product)

# Run Server
if __name__ == '__main__':
  app.run()