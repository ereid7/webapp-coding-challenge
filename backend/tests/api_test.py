
import unittest
import sys
sys.path.append('../src')

import api

class TestProductsApi(unittest.TestCase):
  def setUp(self):
    self.app = api.app.test_client()
    
  # Returns true if the 'get' endpoint returns status code 200
  def test_get_products(self):
    response = self.app.get('/')
    assert response.status_code == 200
  
  # Returns true if the 'put' endpoint returns status code 200
  # when passing name + ingredients params
  def test_create_product(self):
    name = 'productName'
    ingredients = 'ingredient1,ingredient1'
    response = self.app.put(f'/?name={name}&ingredients={ingredients}')
    assert response.status_code == 200

  # Returns true if the 'put' endpoint returns status code 200
  # when passing name param (no ingredients)
  def test_create_product_no_ingredients(self):
    name = 'productName'
    response = self.app.put(f'/?name={name}')
    assert response.status_code == 200

  # Returns true if the put endpoint returns status code 400
  # when no name param is passed
  def test_create_product_invalid_args(self):
    response = self.app.put('/')
    assert response.status_code == 400

if __name__ == "__main__":
    unittest.main()