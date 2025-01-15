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
    
    col1, col2, col3, col4 = st.columns(4) 
    # using Postimages to host the file on platforms to get direct links, aka raw image links
    
    with col1:
        st.image("https://i.postimg.cc/zX3KtqPz/Self-love-quote.jpg", use_container_width=True)
        st.image("https://i.postimg.cc/xT32KpbC/thomas-gibson.jpg", use_container_width=True)

    with col2:
        st.image("https://i.postimg.cc/QN1sFf1J/Essas-vaquinhas-peludas-va-o-te-fazer-explodir-de-tanta-fofura.jpg", use_container_width=True)
        st.image("https://i.postimg.cc/J0GxX3NC/48edb25c-3772-4990-ac7f-9b43609409bd.jpg", use_container_width=True)
        st.image("https://i.postimg.cc/50szYSqk/Cute.jpg", use_container_width=True)

    with col3:
        st.image("https://i.postimg.cc/BnvXMphd/3c95632c-5ee5-46e5-8d54-05c1367f1366.jpg", use_container_width=True)
        st.image("https://i.postimg.cc/8zLnXdjm/giraffe.jpg", use_container_width=True)

    with col4: #video import using imagekit to convert downloaded MP4 into a direct link
        st.video("https://media-hosting.imagekit.io//0b1718ff19894c67/v12044gd0000crac887og65urs7ao4n0.mp4?Expires=1831385035&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=fK2JUA2Lj6lkbahQrJ-q~qRbFDUwZbZjekltrbFWq107Dg835LEBYCAcRN6ce3zfYLaYsCFfeQxWrmu8EelyO1Jb-zC1DnJ0swZLkIFgoOP7FSQogsiMzCRswljQ4xwVZda4hQGy4C4wNZm8-fdiJhDoAU7MLX6IqY7D89saSiocJkJOWP0ojdd3jUzLqjr07LM17HRPF9Yy5lkDMh9g8BdFgu3p-Z37mRVY-NF1KWCpoy4YUdN7Dt~aeMzlkcuGlHb4DEgrYsoJHJrjNEIKyPGJwotmSbenteHJsYqFFNUxAbgi0VOWMim6Fu2z5GaFmEq0U8~q~kIW-3jRHm-nvA__", start_time=0, format="mp4")
        st.image("https://i.postimg.cc/6QsggdZS/Matthew-Gray-Gubler.jpg", use_container_width=True)