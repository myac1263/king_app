import streamlit as st
from PIL import Image
import os

st.set_page_config(
    page_title="The King Application",
    page_icon="👑",  
    layout="wide"  
)

def display_Home_panel():
    #header image
    st.image("https://i.postimg.cc/DfdZgK9y/Screenshot-2025-01-11-at-6-16-28-PM.png", use_container_width=True)
    st.markdown("---")

    st.title("Welcome to The King Application!")
    st.write("Here's some motivation as you enter the IB Testing Application process! Don't forget to look at the baby animals they're amazing!!! 🥳 ")
    
    col1, col2, col3 = st.columns(3) # allows for 3 columns
    # using Postimages to host the file on platforms to get direct links, aka raw image links
    
    with col1:
        st.image("https://i.postimg.cc/zX3KtqPz/Self-love-quote.jpg", use_container_width=True)
        st.image("https://i.postimg.cc/8CzvqDZP/image.jpg", use_container_width=True)

    with col2:
        st.image("https://i.postimg.cc/bwgKgHGS/image.jpg", use_container_width=True)
        st.image("https://i.postimg.cc/J0GxX3NC/48edb25c-3772-4990-ac7f-9b43609409bd.jpg", use_container_width=True)

    with col3:
        st.image("https://i.postimg.cc/BnvXMphd/3c95632c-5ee5-46e5-8d54-05c1367f1366.jpg", use_container_width=True)
        st.image("https://i.postimg.cc/8zLnXdjm/giraffe.jpg", use_container_width=True)