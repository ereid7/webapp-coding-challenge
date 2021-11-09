import psycopg2
from config import productinfo_config
from models import Product

def execute_commands(commands):
  conn = None
  try:
    # read the connection parameters
    params = productinfo_config()
    # connect to the PostgreSQL server
    conn = psycopg2.connect(params)
    cur = conn.cursor()
    # create table one by one
    for command in commands:
        cur.execute(command)
    # close communication with the PostgreSQL database server
    cur.close()
    # commit the changes
    conn.commit()
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  finally:
    if conn is not None:
      conn.close()
      
def get_products():
  products = []
  get_products_query = "SELECT product_id, product_name FROM product"
  conn = None
  try:
      params = productinfo_config()
      conn = psycopg2.connect(params)
      cur = conn.cursor()
      cur.execute(get_products_query)
      row = cur.fetchone()

      while row is not None:
          products.append(Product(row[0], row[1], []))
          row = cur.fetchone()
      cur.close()
  except (Exception, psycopg2.DatabaseError) as error:
      print(error)
  finally:
      if conn is not None:
          conn.close()

  # fetch ingredients for each product
  for product in products:
    product.ingredients = get_ingredients(product.product_id)

  return products

def get_ingredients(product_id):
  get_ingredients_query = (
    f"""
    SELECT ingredient.ingredient_id, ingredient.ingredient_name
    FROM product_ingredient
    INNER JOIN ingredient
    	ON ingredient.ingredient_id = product_ingredient.ingredient_id
    WHERE product_ingredient.product_id = {product_id}
    """
  )
  ingredients = []
  conn = None
  try:
      params = productinfo_config()
      conn = psycopg2.connect(params)
      cur = conn.cursor()
      cur.execute(get_ingredients_query)
      row = cur.fetchone()
      while row is not None:
        ingredients.append(row[1])
        row = cur.fetchone()
      cur.close()
  except (Exception, psycopg2.DatabaseError) as error:
      print(error)
  finally:
      if conn is not None:
          conn.close()
  return ingredients
  
def create_product(product_name, ingredient_names):
  insert_product_commands = (
    f"""
    INSERT INTO product(product_name)
    VALUES ('{product_name}') 
    ON CONFLICT DO NOTHING
    """,
  )

  execute_commands(insert_product_commands)
  for ingredient_name in ingredient_names:
    insert_ingredients_commands = (
    f"""
    INSERT INTO ingredient(ingredient_name)
    VALUES ('{ingredient_name}') 
    ON CONFLICT DO NOTHING""",
    f"""
    INSERT INTO product_ingredient(product_id, ingredient_id)
    VALUES (  
	    (select product_id from product where product_name = '{product_name}'), 
        (select ingredient_id from ingredient where ingredient_name = '{ingredient_name}')
      )
    ON CONFLICT DO NOTHING;
    """)
    execute_commands(insert_ingredients_commands)

if __name__ == '__main__':
  get_products()