import requests

lotto_url = 'https://www.10000recipe.com/'
raw = requests.get(lotto_url)
print(raw.text)