from PIL import Image
import requests
import streamlit as st

st.set_page_config(page_title="Podcast Project", page_icon=":love_letter:", layout="wide")

# Load Assets
img_wib_podcast = Image.open("images/Pink Illustrative Podcast Logo.png")
graphic1 = "https://github.com/mmichelle1779/Michelle-Portfolio/blob/main/images/Podcast%20Project%20Infographic/1.png"
graphic2 = "https://github.com/mmichelle1779/Michelle-Portfolio/blob/main/images/Podcast%20Project%20Infographic/2.png"

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

# Product Vision
with st.container():
    text_column, image_column = st.columns((3.5, 1))
    with image_column:
        st.image(graphic1, width=300)
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

# Product Roadmap
st.subheader("Product Roadmap")

# Product Strategy
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(graphic2, width=300)
    with text_column:
        st.subheader("Product Strategy")
        st.write(
            """
            1. **Audience-Centric Content:** Deliver high-value content that resonates with aspiring women in business, 
            focusing on leadership, innovation, and career development.
            2. **Engagement & Feedback Loop:** Regularly survey student members to identify topic interests and guest 
            preferences, ensuring content remains relevant and engaging.
            3. **Collaborative Promotion:** Collaborate with Marketing and Finance Committees to boost visibility through 
            social media, Slack channels, and newsletters while efficiently allocating the budget.
            4. **Cross-Functional Collaboration:** Align podcast goals with organizational objectives, working closely 
            with the WIB External Committee, studio technicians, and marketing teams for seamless production and promotion.
            5. **Scalable Growth:** Plan for content expansion with new series and themes, and explore partnerships and 
            sponsorships to support long-term growth and broaden reach.
            """
        )


# Draft 1



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