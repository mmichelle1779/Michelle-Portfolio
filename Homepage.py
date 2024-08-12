from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Find emojis here: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.set_page_config(page_title="Michelle's Homepage", page_icon=":love_letter:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Assets
lottie_coding = load_lottieurl("https://lottie.host/5755b802-5e4d-4e48-b1de-847e86f2ab3c/VuE4W5i6Tp.json")
img_win_conference = Image.open("images/WIB Annual Business Conference Itinerary.png")
img_wib_podcast = Image.open("images/Pink Illustrative Podcast Logo.png")

# Sidebar Menu
st.sidebar.empty()

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
        st.write("Navigate to my projects or "
                 "check out my [LinkedIn](https://www.linkedin.com/in/michelle-m-mar/).")
    with right_column:
        st.lottie(lottie_coding, height=300, key="coding")

# Projects
st.write("---")
st.title("My Projects")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_wib_podcast)
    with text_column:
        st.subheader("Women In Business Podcast: You Heard Her")
        st.write(
            """
            The UCSD Women in Business podcast is dedicated to highlighting the journeys and achievements of inspiring 
            women in various industries. Through in-depth interviews, the podcast explores their career paths, 
            challenges, and successes, offering valuable insights and advice to listeners. The goal is to empower and 
            inspire women in the business world by sharing stories of leadership, innovation, and resilience, creating 
            a platform for diverse voices and perspectives.
            """
        )
        st.write("Click [here](https://michelle-portfolio.streamlit.app/Podcast_Project) to learn more.")
        st.markdown("Spotify Podcast link coming soon!")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_win_conference)
    with text_column:
        st.subheader("Women In Business 2024 Annual Winter Conference: Beyond the Blueprint")
        st.write(
            """
            The 2024 Annual Winter Conference: Beyond the Blueprint aimed to explore key business fields—Marketing, 
            Product Management, Finance, and Human Resources—offering attendees valuable insights and networking 
            opportunities. Held on March 9, 2024, from 12 PM to 3:30 PM at Joya Kitchen, the event featured 17 
            industry professionals from leading companies such as Deloitte, Google, Wells Fargo, Illumina, and Meta. 
            The conference included networking sessions, panel discussions, and Q&A opportunities, with snacks provided 
            and a business professional dress code. The goals were to facilitate knowledge sharing on various business 
            fields, provide a platform for networking, and offer practical takeaways and opportunities for interaction. 
            The event aimed to enhance attendees' understanding of industry trends and career paths while strengthening 
            their professional networks.
            """
        )
        st.markdown("Click [here](https://drive.google.com/drive/folders/12yZrD5miL4K8h8b0P833YPDFYZv-099s) to learn more.")
