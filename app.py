from PIL import Image
import requests
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie

# Find emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Michelle's Webpage", page_icon=":love_letter:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# Load Assets
lottie_coding = load_lottieurl("https://lottie.host/5755b802-5e4d-4e48-b1de-847e86f2ab3c/VuE4W5i6Tp.json")
img_win_conference = Image.open("images/WIB Annual Business Conference Itinerary.png")
img_wib_podcast = Image.open("images/Pink Illustrative Podcast Logo.png")

# Horizontal Menu
 selected = option_menu(
    menu_title=None, #required
    options=["Home", "Projects", "Contact"], #required
    icons=["house", "book", "envelope"], #optional
    menu_icon="cast", #optional
    default_index=0, #optional
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "white"},
        "icon": {"color": "orange", "font-size": "25px"},
        "nav-link": {
            "font-size": "25px",
            "text-align": "left",
            "margin": "0px"
            "--hover-color": "#eee",
        },
        "nav-link-selected": {"background-color": "white"},
    }
 )

if selected == "Home":
    st.title(f"You have selected {selected}")
if selected == "Projects":
    st.title(f"You have selected {selected}")
if selected == "Contact":
    st.title(f"You have selected {selected}")

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
        st.write("Check out my [LinkedIn](https://www.linkedin.com/in/michelle-m-mar/).")
    with right_column:
        st.lottie(lottie_coding, height=300, key="coding")

# Projects
with st.container():
    st.write("---")
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


# Contact
with st.container():
    st.write("---")
    st.header("Get in touch with me!")
    st.write("##")

    # Documentation: https://formsubmit.co/
    contact_form = """
    <form action="https://formsubmit.co/mimar@ucsd.edu" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()