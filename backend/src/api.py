from flask import Flask
from flask_restful import reqparse, abort, Resource, Api
from flask_cors import CORS, cross_origin
from repository import get_products, create_product
import json

app = Flask(__name__)
CORS(app, support_credentials=True)
api = Api(app)

# initialize request parser
parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('ingredients')

class ProductsApi(Resource):
  @cross_origin(supports_credentials=True)
  def put(self):
    args = parser.parse_args()
    # read name argument
    name = args['name']

    # do not create product if name is empty
    if not name:
      return {}, 400

    # read ingredients argument
    ingredients = []
    if (args['ingredients']):
      ingredients = args['ingredients'].split(',')

    # create product in db
    create_product(name, ingredients)
    return {}, 200

  @cross_origin(supports_credentials=True)
  def get(self):
    return json.dumps([product.toJson() for product in get_products()])

api.add_resource(ProductsApi, '/')

if __name__ == '__main__':
  app.run(debug=True)