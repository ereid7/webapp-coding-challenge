class Product(object):
  product_id = ""
  name = ""
  ingredients = []

  def __init__(self, product_id, name, ingredients):
    self.product_id = product_id
    self.name = name
    self.ingredients = ingredients

  def toJson(self):
    return {"product_id": self.product_id, "name": self.name, "ingredients": self.ingredients}