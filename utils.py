"""
 AUTHOR: Diego Salas Noain/Diane Renard
 FILENAME: utils.py
 SPECIFICATION: Functions to parse and scrape information from different walmart urls
 FOR: CS 5364 Information Retrieval Section 001
"""

import json
import time
from typing import List
import winsound
import requests
from urllib.parse import urlencode
from parsel import Selector
from loguru import logger as log
import pandas as pd
from pandas import DataFrame
from constants import *
from cookies import *

"""
 NAME: create_search_url
 PARAMETERS: query, page, sort
 PURPOSE: The function creates a url for a single walmart search page
 PRECONDITION: The query should be non empty
 POSTCONDITION: Return the new url string
"""
def create_search_url(query: str, page=1, sort="price_low") -> str:
    return "https://www.walmart.com/search?" + urlencode(
        {
            "q": query,
            "sort": sort,
            "page": page,
            "affinityOverride": "default",
        }
    )

"""
 NAME: parse_search
 PARAMETERS: html_text
 PURPOSE: The function extract search results from search HTML response
 PRECONDITION: The given HTML text should not be empty
 POSTCONDITION: The number of products will be returned as well as the information about each of them
"""
def parse_search(html_text: str):
    sel = Selector(text=html_text)
    data = sel.xpath('//script[@id="__NEXT_DATA__"]/text()').get()
    data = json.loads(data)

    total_results = data["props"]["pageProps"]["initialData"]["searchResult"]["itemStacks"][0]["count"]
    results = data["props"]["pageProps"]["initialData"]["searchResult"]["itemStacks"][0]
    return results, total_results

"""
 NAME: parse_product
 PARAMETERS: html_text
 PURPOSE: The function parse a walmart product from the product page response
 PRECONDITION: The given HTML text should not be empty
 POSTCONDITION: If no product found, it does not return anything, else it returns the product information
"""
def parse_product(html_text: str):
    sel = Selector(text=html_text)
    data = sel.xpath('//script[@id="__NEXT_DATA__"]/text()').get()
    if data != None: # This verification is because we might get an html with no content
        data = json.loads(data)
        _product_raw = data["props"]["pageProps"]["initialData"]["data"]["product"]
        wanted_product_keys = [
                               "averageRating", # rating
                               "brand",
                               "imageInfo", # thumbnail_image
                               "manufacturerName", # manufacturer
                               "name",
                               "model",
                               "priceInfo", # price
                               "shortDescription", # description
                               "reviews" # comments
                               "type",] # type_of
        
        if _product_raw == None: 
            return
        
        product = {k: v for k, v in _product_raw.items() if k in wanted_product_keys}
        reviews_raw = data["props"]["pageProps"]["initialData"]["data"]["reviews"]
        product['reviews'] = reviews_raw
        return product

"""
 NAME: scrape_products_by_url
 PARAMETERS: urls, df
 PURPOSE: The function scrape walmart products by using their urls
 PRECONDITION: The url list is not empty but the df is.
 POSTCONDITION: >It returns a populated dataframe 
"""
def scrape_products_by_url(urls: List[str], df: DataFrame) -> DataFrame:
    """scrape walmart products by urls"""
    log.info(f"scraping {len(urls)} product urls (in chunks of 50)")
    i = 0
    fileNum = 1
    for url in urls:                                             #urls is the file containing multiple url
        i += 1
        html = requests.get(url, headers=headers_product_detail) #headers are important because they might hid the fact that this is an actual bot
        product = parse_product(html.text)
        time.sleep(10) # fake being a real user
        if product != None:
            df = df.append(pd.json_normalize(product), ignore_index=True)
        
        if html.status_code == 200:
            http_status = 'Successfully'
        else:
            http_status = 'Unsuccessfully'
            beep()
            if f'cookie{fileNum}' in cookies:
                headers_product_detail['cookie'] = cookies[f'cookie{fileNum}']
                fileNum += 1
            else:
                break

        log.info(f'Scraped {url} {http_status} waiting...')    
    return df

"""
 NAME: beep
 PARAMETERS: none
 PURPOSE: The function indicates by an audio beep, that walmart has blocked our request
 POSTCONDITION: The developper is alerted via an audio beep
"""
def beep():
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 1000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)