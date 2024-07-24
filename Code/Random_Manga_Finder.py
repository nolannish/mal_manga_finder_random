import requests
import random
import json

RAND_INT = random.randint(1, 1000)
response = requests.get(f'https://api.jikan.moe/v4/manga/{RAND_INT}')

response_dict = response.json()

y = json.dumps(response_dict, indent=4, sort_keys=True)
x = json.loads(y)

print(x["data"]["mal_id"])
print(x["data"]["title"])
print(x["data"]["rank"])
print(x["data"]["authors"][0]["name"])
