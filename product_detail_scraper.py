import pandas as pd
from urllib.parse import urljoin
from utils import *
from constants import *

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
products.to_csv('walmart-products.csv')