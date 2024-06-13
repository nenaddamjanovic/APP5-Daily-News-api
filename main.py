import requests

api_key = "739c22320f334af89c77e6b5e5580dc8"
url = ("https://newsapi.org/v2/everything?q=tesla&"
       "from=2024-05-13&sortBy=publishedAt&"
       "apiKey=739c22320f334af89c77e6b5e5580dc8")

# Make request
request = requests.get(url)
# content = request.text  Ovi podaci su samo string

# Get a dictionary with data
content = request.json()  # Ovi podaci su rečnik

# Access the article titles and descriptions
for article in content["articles"]:
    print(article["title"])
    print(article["descriptions"])

