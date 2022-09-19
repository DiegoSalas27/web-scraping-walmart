import json
import pandas as pd

with open('response.json', 'r') as f:
  data = json.load(f)

df = pd.json_normalize(data['items'])

print(df.head())

# for item in data['items']:
#   try:
#     print(
#       item['canonicalUrl'], 
#       item['description'], 
#       item['image'], 
#       item['name'], 
#       item['price'],
#       item['rating']['averageRating'],
#       item['rating']['numberOfReviews'],
#     )
#   except:
#     pass