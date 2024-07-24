import requests
import json
import random

RAND_INT = random.randint(1, 1000)

response = requests.get(f'https://api.spotify.com/v1/albums/{RAND_INT}')

print(response.status_code)