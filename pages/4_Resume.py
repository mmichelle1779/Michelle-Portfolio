from pathlib import Path
import streamlit as st
from PIL import Image
import io

# Path Settings
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Michelle Mar Resume.pdf"

# General Settings
PAGE_TITLE = "Resume | Michelle Mar"
PAGE_ICON = ":love_letter:"
NAME = "Michelle Mar"
DESCRIPTION = """
Undergraduate Student at UCSD
"""
EMAIL = "mimar@ucsd.edu"
PROJECTS = {
    "Women In Business Podcast: You Heard Her"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Load CSS
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# Load Resume
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# URL for Headshot
url = "https://raw.githubusercontent.com/mmichelle1779/Michelle-Portfolio/main/pages/assets/Michelle%20LinkedIn%20Headshot.png"

# Hero Section
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(url, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )