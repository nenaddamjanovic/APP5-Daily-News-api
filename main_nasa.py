import requests
import streamlit as st

st.set_page_config(layout="wide")

# Prepare Api key and url
nasa_api_key = "3adHWnXwwNn1cwFEFAmSw0jr3FVHN31d3zbcncUj"
nasa_url = (f"https://api.nasa.gov/planetary/apod?api_key={nasa_api_key}"
            f"&count=5"
            f"&concept_tags=True")

# Get request data as dictionary
response1 = requests.get(nasa_url)
data = response1.json()

st.title("Mali sajt za moju pilu od NASE")
st.write("Ovde izlaze random 5 slika iz Nasine galerije slika, sa datumom fotografije i opisom")

# Extract the image, url, and explanation from data
for i, d in enumerate(data):
    title = d["title"]
    image_url = d["url"]
    explanation = d["explanation"]
    date_of_image = d["date"]

    # Download image
    image_filepath = f"img{i}.png"  # Biće naziv slike
    response2 = requests.get(image_url)
    with open(image_filepath, "wb") as file:  # čuva sliku u ime fajla
        file.write(response2.content)

    st.header(title)
    st.write(date_of_image)
    st.image(image_filepath)
    st.write(explanation)
    st.divider()

st.write("Znaš da te volim do ovih zvezda i nazad <3")