from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Find emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Michelle's Homepage", page_icon=":love_letter:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Assets
lottie_coding = load_lottieurl("https://lottie.host/5755b802-5e4d-4e48-b1de-847e86f2ab3c/VuE4W5i6Tp.json")

# Sidebar Menu
st.sidebar.success("Select a page above.")

# Header Section
with st.container():
    st.title("Hello! My name is Michelle :wave:")
    st.write("And I am an aspiring Product Manager.")

# What I Do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About Me")
        st.write(
            """
            My name is Michelle and I am an undergraduate student at UC San Diego majoring in Business Economics 
            with a minor in Data Science. My dream is to go into Product Management. 
            As a young, entrepreneurial thinker who has a great deal of interest in design thinking, I value having a 
            growth mindset and am always searching for new opportunities and experiences I can learn and grow from. 
            If you would like to connect with me or have any questions, please contact me through my email: 
            mimar@ucsd.edu.
            """
        )
        st.write("Want to learn more?")
        st.write("Navigate to my [projects](https://michelle-portfolio.streamlit.app/Projects) or "
                 "check out my [LinkedIn](https://www.linkedin.com/in/michelle-m-mar/).")
    with right_column:
        st.lottie(lottie_coding, height=300, key="coding")
