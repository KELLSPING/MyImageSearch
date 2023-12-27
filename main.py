import requests

# this API with free version is 100 searches per day

API_KEY = open('./API_KEY').read()
SEARCH_ENGINE_ID = open('./SEARCH_ENGINE_ID').read()

search_query = '蘋果'

url = 'https://www.googleapis.com/customsearch/v1'
params = {
    'q':search_query,
    'key':API_KEY,
    'cx':SEARCH_ENGINE_ID,
    'search_type':'image',
    'lr':'lang_en',
    'gl':'US'
}

response = requests.get(url, params=params)
results = response.json()['items']

for item in results:
    print(item['link'])