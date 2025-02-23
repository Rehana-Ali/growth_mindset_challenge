import streamlit as st
import requests

# Pexels API key (replace with your own key)
PEXELS_API_KEY = "DNrhl8sBXWKJMnS1gKlUI3RjcLbwlOklQQhUlQD33CGT6NmEC8J8IpVC"
PEXELS_API_URL = "https://api.pexels.com/v1/search"
PIXABAY_API_KEY = "49016224-c8ef8a6dda00a3cd813f5666f"
PIXABAY_API_URL = "https://pixabay.com/photos/example"

# Function to fetch images from Pexels API
def fetch_images(query, per_page=10):
    headers = {"Authorization": PEXELS_API_KEY}
    params = {"query": query, "per_page": per_page}
    response = requests.get(PEXELS_API_URL, headers=headers, params=params)

    if response.status_code == 200:
        return response.json().get("photos", [])
    else:
        return []

# Streamlit UI
st.title("Image Search App using Streamlit")
search_query = st.text_input("Enter a keyword to search images", "nature")

if st.button("Search"):
    images = fetch_images(search_query)
    
    if images:
        st.write(f"Showing results for: **{search_query}**")
        cols = st.columns(3)  # 3 images per row
        for i, image in enumerate(images):
            with cols[i % 3]:  # Place images in columns
                # Updated: Replaced use_column_width with use_container_width
                st.image(image["src"]["medium"], caption=image["photographer"], use_container_width=True)
    else:
        st.error("No images found. Try another search!")

# Footer
st.markdown("---")
st.markdown("Built with using Streamlit")
