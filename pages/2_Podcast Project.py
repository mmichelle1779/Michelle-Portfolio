from PIL import Image
import requests
import streamlit as st

st.set_page_config(page_title="Podcast Project", page_icon=":love_letter:", layout="wide")

# Load Assets
img_wib_podcast = Image.open("images/Pink Illustrative Podcast Logo.png")
graphic1 = ("images/Podcast Project Infographic/1.png")
graphic2 = ("images/Podcast Project Infographic/2.png")
graphic3 = ("images/Podcast Project Infographic/3.png")
product_roadmap1 = ("images/product roadmap/1.png")
product_roadmap2 = ("images/product roadmap/2.png")

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

# Product Vision
with st.container():
    st.write("---")
    st.subheader("Product Vision")
    text_column, image_column = st.columns((3.5, 1))
    with image_column:
        st.image(graphic1)
    with text_column:
        st.write(
            """
            To create a leading platform that empowers and inspires women in business by sharing diverse stories of 
            leadership, innovation, and resilience. The podcast aims to bridge the gap between aspiring professionals 
            and industry leaders by providing valuable insights, actionable advice, and a sense of community, ultimately 
            fostering the growth and success of women in various fields. Through engaging and in-depth interviews, the 
            podcast will become a trusted resource for listeners seeking inspiration and guidance in navigating their 
            career paths.
            """
        )

# Product Roadmap
st.write("---")
st.subheader("Product Roadmap")
st.image(product_roadmap1)
st.image(product_roadmap2)

# Product Strategy
with st.container():
    st.write("---")
    st.subheader("Product Strategy")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(graphic2)
    with text_column:
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

# Market Research & Go-to-Market Strategy
with st.container():
    st.write("---")
    st.subheader("Market Research & Go-to-Market Strategy")
    text_column, image_column = st.columns((3.5, 1))
    with image_column:
        st.image(graphic3)
    with text_column:
        st.write(
            """
            - Conducted surveys among student members to identify key topics, industries, and roles of interest, 
            ensuring podcast content aligns with audience demand.
            - Leveraged survey insights to craft a personalized content strategy, selecting guest speakers and 
            tailoring episode themes accordingly.
            - Developed a go-to-market strategy, including targeted outreach through social media and the 
            organization’s Slack channel, to maximize listener engagement.
            - Coordinated with the Marketing and Finance Committees to manage promotion and budget, resulting 
            in a 40% increase in visibility and listener engagement.
            """
        )