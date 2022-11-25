import requests
import username as username
import json

username - "laidlara"
url = "https://api.github.com/users/{}".format(username)

response = requests.get(url)

output = json.loads(response.text)

print(output)
