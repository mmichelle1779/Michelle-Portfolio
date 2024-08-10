from PIL import Image
import requests
import streamlit as st

st.set_page_config(page_title="Contact Info", page_icon=":love_letter:", layout="wide")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# Find emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/

# Contact Info
with st.container():
    st.header("My Contact Info")
    st.write(":telephone_receiver: : (408) 234-1779")
    st.write(":love_letter: : mimar@ucsd.edu")

# Contact Form
with st.container():
    st.write("---")
    st.header("Get in touch with me!")

    # Documentation: https://formsubmit.co/
    contact_form = """
    <form action="https://formsubmit.co/mmichelle1779@gmail.com" method="POST">
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