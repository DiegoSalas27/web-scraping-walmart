import requests
import pandas as pd
import time # fake you are a real user
import math
from loguru import logger as log
from utils import *

# dynamic url creation
url = create_search_url(query='spider')

# headers for walmart page
headers = {
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
  "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
  "accept-language": "en-US;en;q=0.9",
  "accept-encoding": "gzip, deflate, br",
}

# create dataFrame
products = pd.DataFrame([])

# Perform initial request (it's necessary to get correct pagination)
html = requests.get(url, headers=headers) # response is html
results, total_items = parse_search(html.text)

# Get number of pages
max_page = math.ceil(total_items / 40) # 40 products per page
log.info(f"found total {max_page} pages of results ({total_items} products)")
if max_page > 25:
    max_page = 25

# Get all products from each page
for i in range(2, max_page + 1):
  url = create_search_url(query='spider', page=i)
  html = requests.get(url, headers=headers) # response is html
  results = parse_search(html.text)[0] # here we only care about the products
  products = products.append(pd.json_normalize(results['items']), ignore_index=True)
  time.sleep(5)
  print(f'Getting page {i}', 'waiting...')

# Save our product data in csv file
products.to_csv('walmart-products.csv')

# TODO: get for each product page based on collected products


# Testing files
# print(df.head())

# with open('result.html', 'w') as f: 
#   f.write(html.text)

# with open('response.json', 'w') as f:
#   f.write(json.dumps(results))