"""
 AUTHOR: Diego Salas Noain/ Diane Renard
 FILENAME: product_detail_scrapper.py
 SPECIFICATION: How do we scrape the specific details of a product from the list of product returned? 
                We  go to the specific page of the product and scrape the details 
 FOR: CS 5364 Information Retrieval Section 001
"""

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

df = pd.read_csv('walmart-products-preview.csv')

# get each product page based on collected products

# create dataFrame
products = pd.DataFrame([])

# get urls for each product
product_urls = []
for canonicalUrl in df['canonicalUrl']:
  try:
    product_urls.append(urljoin("https://www.walmart.com/", canonicalUrl) )
  except:
    continue

products = scrape_products_by_url(product_urls, products)


# save each dataframe row in the database
for index, row in products.iterrows():
  try:
    sql = "INSERT INTO products (category_id, name, product_slug, brand, model, description, manufacturer, thumbnail_image, rating, price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (
      1,
      row['name'], 
      row['name'],
      row['brand'], 
      row['model'], 
      row['shortDescription'], 
      row['manufacturerName'], 
      row['imageInfo.thumbnailUrl'], 
      row['averageRating'], 
      row['priceInfo.currentPrice.price'])

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
  except:
    continue