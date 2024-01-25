import requests

# Set the URL of the script.js file in the GitHub repository
url = "https://raw.githubusercontent.com/authifyWeb/filters/main/URL/filters.js"

# Send an HTTP GET request to retrieve the file
response = requests.get(url)

# Write the retrieved data to a new file
with open("./fame/filters.js", "w") as f:
    f.write(response.text)
