from PIL import Image
import requests
import streamlit as st
from streamlit_option_menu import option_menu

# Load Assets
img_win_conference = Image.open("images/WIB Annual Business Conference Itinerary.png")
img_wib_podcast = Image.open("images/Pink Illustrative Podcast Logo.png")

# Projects
with st.container():
    st.header("My Projects")
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
        st.markdown("[Click here to learn more.](https://drive.google.com/drive/folders/1BLgSdXOvQPych6WH-JIvwpyJgpMPhtWb)")
