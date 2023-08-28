# poc-walmart
This projects implements evading IP tracking by rotating residential proxies via VPN, Updating cookies. This techniques should allow us to scrape through Walmart website without being blocked. Used for educational purposes only

## Environment variables:
It will be necessary to create an .env file in the root of this project with the following entries:
```
DB_HOST=<address of the host>(could be localhost if the database is running on the same computer)
DB_PASSWORD=<password for the database user>
DB_USER=<name of the user of the database>
DB_NAME=<name of the database to use>
```

## install dependencies:
```
pip install -r requirements.txt
```

## Run this project:
You will first need to run the product_grid_scraper file as it will retrieve the cannonicalUrls for each product in a given category and store them in a csv file (this urls points to a product description):
```
python product_grid_scraper.py
```
You will then get a preview csv file that will be read by the product_detail_scraper file. To run this file enter this command:
```
python product_detail_scraper.py
```
