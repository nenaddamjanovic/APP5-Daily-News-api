import requests
from send_email import send_mail

topic = "tesla"

api_key = "739c22320f334af89c77e6b5e5580dc8"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "from=2024-05-13&"
       "sortBy=publishedAt&"
       "apiKey=739c22320f334af89c77e6b5e5580dc8&"
       "language=en")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()  # Ovi podaci su rečnik

# # Compose message content using fstring
# message_body = ""
# # Access the article titles and descriptions
# for article in content["articles"][:20]:
#     # Create mail body using fstring
#     # Koristimo fstring zbog greške NoneObj
#     message_body = (f"{message_body}{article["title"]}"
#                     f"\n{article["description"]}"
#                     f"\n{article["url"]}\n-\n")
# Create mail message using fstring
# message = f"Subject: Today news\n\n{message_body}"

# Compose message content using fstring
body = ""

for article in content["articles"][:20]:
    if article["title"] is not None:
        body = ("Subject: Todays News" + "\n" + body
                + article["title"] + "\n"
                + article["description"] + "\n"
                + article["url"] + 2*"\n")

# Zbog moguće UTF-8 greške
message = body.encode("utf-8")

send_mail(message=message)

