from PIL import Image
import requests
import streamlit as st

st.set_page_config(page_title="Annual Winter Conference", page_icon=":love_letter:", layout="wide")

# Load Assets
img_win_conference = Image.open("images/WIB Annual Business Conference Itinerary.png")

st.title("Women In Business 2024 Annual Winter Conference: Beyond the Blueprint")
st.write("---")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_win_conference)
    with text_column:
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
