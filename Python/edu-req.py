import requests

r = requests.get('https://www.spacejam.com/1996/', stream=True)

print(r.raw.read())
