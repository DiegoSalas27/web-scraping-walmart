import os
import mysql.connector
import pandas as pd
from urllib.parse import urljoin
from utils import *
from constants import *
from dotenv import load_dotenv
load_dotenv('.env')

# connect to database
mydb = mysql.connector.connect(
  host=os.getenv('DB_HOST'),
  user=os.getenv('DB_USER'),
  password=os.getenv('DB_PASSWORD'),
  database=os.getenv('DB_NAME'),
)

mycursor = mydb.cursor()

# get products from csv file

df = pd.read_csv('target_new_479products.csv', encoding='latin1')

for index, row in df.iterrows():
  try:
    sql = "INSERT INTO products (category_id, name, product_slug, brand, model, description, manufacturer, thumbnail_image, rating, price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (
      1,
      row['name'], 
      row['product_slug'],
      row['brand'], 
      row['model'], 
      row['description'], 
      row['manufacturer'], 
      row['thumbnail_image'], 
      row['rating'], 
      row['price'])

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
  except:
    continue

# products.to_csv('walmart-products-detail.csv')