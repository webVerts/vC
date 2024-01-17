import requests

Source Repo 
url = "https://raw.githubusercontent.com/authifyWeb/filters/main/URL/filters.js"

response = requests.get(url)

Desination Repo
with open("./fame/filters.js", "w") as f:
    f.write(response.text)
