from pathlib import Path

import streamlit as st
from PIL import Image

# Path Settings
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current dir / "styles" / "main.css"
resume_files = current_dir / "assets" / "Michelle Mar Resume.pdf"
profile_pic = current_dir / "assets" / "Michelle LinkedIn Headshot.jpg"

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

st.title("Hello there!")