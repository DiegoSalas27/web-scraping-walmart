"""
 AUTHOR: Diego Salas Noain/Diane Renard
 FILENAME: product_grid_scraper.py
 SPECIFICATION: How do we scrape a list of products that goes on different pages? 
                Scrape through each of the pages by usings request package and parse the data using parsel.
 FOR: CS 5364 Information Retrieval Section 001
"""

import requests
import pandas as pd
import time
import math
from loguru import logger as log
from utils import *
from constants import *

# dynamic url creation
url = create_search_url(query='televisions') # dynamic url creation

# create dataFrame
products = pd.DataFrame([]) # create dataFrame

# Perform initial request (it's necessary to get correct pagination)
html = requests.get(url, headers=headers) # response is html
results, total_items = parse_search(html.text)

products = products.append(pd.json_normalize(results['items']), ignore_index=True)

# Get number of pages
max_page = math.ceil(total_items / 40) # 40 products per page
log.info(f"found total {max_page} pages of results ({total_items} products)")
if max_page > 25:
    max_page = 25

# Get all products from each page starting from 2
for i in range(2, max_page + 1):
  url = create_search_url(query='televisions', page=i)
  html = requests.get(url, headers=headers) # response is html
  results = parse_search(html.text)[0] # here we only care about the products
  products = products.append(pd.json_normalize(results['items']), ignore_index=True)
  time.sleep(5) # fake being a real user
  print(f'Getting page {i}', 'waiting...')

# Save our product data in csv file
products = products[['canonicalUrl', 'description', 'image', 'name', 'price', 'rating.averageRating', 'rating.numberOfReviews']]
products.to_csv('walmart-products-preview.csv')