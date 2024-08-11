from PIL import Image
import requests
import streamlit as st

st.set_page_config(page_title="Podcast Project", page_icon=":love_letter:", layout="wide")

# Load Assets
img_wib_podcast = Image.open("images/Pink Illustrative Podcast Logo.png")
podcast_graphic_1 = Image.open("images/Podcast Project Infographic/1.png")
podcast_graphic_2 = Image.open("images/Podcast Project Infographic/2.png")

# Title
st.title("Women In Business Podcast: You Heard Her")
st.write("---")

# Project Info
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_wib_podcast)
    with text_column:
        st.write(
            """
            The UCSD Women in Business podcast is dedicated to highlighting the journeys and achievements of inspiring 
            women in various industries. Through in-depth interviews, the podcast explores their career paths, 
            challenges, and successes, offering valuable insights and advice to listeners. The goal is to empower and 
            inspire women in the business world by sharing stories of leadership, innovation, and resilience, creating 
            a platform for diverse voices and perspectives.
            """
        )
        st.write("Check out my [Project Planning Sheet]"
                 "(https://docs.google.com/document/d/1vDb1Sjt3bEbyKkZzqr4WmFqzDMEAxsDINTeFEkJDUeM/edit#heading=h.gjdgxs)")
        st.write("Check out my [Podcast Outreach Template]"
                 "(https://docs.google.com/document/d/1STOPvyBbjaMcodNlF782AylJrbpTiKd6-vUMfS6Xap0/edit#heading=h.gjdgxs)")
        st.markdown("Spotify Podcast link coming soon!")

# Project Breakdown with Infographics
st.write("---")

# URL for graphics
url = "https://github.com/mmichelle1779/Michelle-Portfolio/blob/main/images/Podcast%20Project%20Infographic/1.png"

with st.container():
    text_column, image_column = st.columns((4, 1))
    with image_column:
        st.image(url, width=230)
    with text_column:
        st.subheader("Product Vision")
        st.write(
            """
            - To create a leading platform that empowers and inspires women in business by sharing diverse stories of 
            leadership, innovation, and resilience. The podcast aims to bridge the gap between aspiring professionals 
            and industry leaders by providing valuable insights, actionable advice, and a sense of community, ultimately 
            fostering the growth and success of women in various fields. Through engaging and in-depth interviews, the 
            podcast will become a trusted resource for listeners seeking inspiration and guidance in navigating their 
            career paths.
            """
        )





# Draft 1


st.write("**Product Strategy:**")
st.write(
    """
    - Developed a comprehensive product strategy aligned with market trends and audience preferences.
    - Conducted outreach and cold emailing/messaging to potential guest speakers.
    - Crafted a personalized question list based on a survey of common questions from student members, tailoring inquiries 
    to the guest’s profession and story.
    - Facilitated recording sessions in the campus podcasting studio to produce high-quality episodes.    
    """
)
st.write("**Roadmap Roadmap:**")
st.write(
    """
    - Created and managed a detailed roadmap for content creation and episode releases, aligning quarterly themes like 
    FinTech and product management with audience demand. This roadmap ensured the timely delivery of episodes and 
    aligned the podcast's growth with its strategic objectives.
    """
)
st.write("**Market Research:**")
st.write(
    """
    - Conducted in-depth market research to identify trending topics and audience interests.
    - Administered surveys to student members to gauge their preferences, including specific industries, roles, career 
    paths, and companies they wanted to learn about.
    - Used survey insights to guide content strategy and guest selection, ensuring alignment with the most relevant and 
    sought-after topics.
    - Crafted tailored question lists for guest speakers based on survey findings, enhancing the relevance and engagement 
    of each episode.
    """
)
st.write("**Go-to-Market Strategy:**")
st.write(
    """
    - Collaborated with the WIB External Committee to align podcast goals with organizational objectives.
    - Coordinated with the Finance Committee to communicate budget costs and ensure financial alignment.
    - Coordinated with studio technicians to ensure the seamless production and distribution of podcast episodes.
    - Worked with the Marketing Committee to promote the podcast through social media and the organization’s Slack channel.
    """
)
st.write("**Impact & Growth:**")
st.write(
    """
    - Continuously iterated based on user feedback, expanding the podcast’s reach and influence by 15% each quarter.
    """
)