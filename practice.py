import requests

api_key = "66429545-af0e-419b-aedb-43ac983ff099"
word = "phone"
url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}"

res = requests.get(url)

definitions = res.json()
for definition in definitions:
    print(definition)
