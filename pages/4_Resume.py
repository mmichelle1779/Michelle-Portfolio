from pathlib import Path
import streamlit as st

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
    st.write(":e-mail: : mimar@ucsd.edu")
    st.write(":mega: : [linkedin.com/in/michelle-m-mar/](https://www.linkedin.com/in/michelle-m-mar/)")

# Skills
st.write("---")
st.subheader("Technical Skills")
st.write(
    """
    - Programming: Python, SQL, Stata, R
    - Data Visualization: MS Excel
    - Databases: MySQL
    - CRM: Salesforce, HubSpot
    """
)

# Certifications
st.subheader("Certifications")
st.write("Google Data Analytics Professional Certificate | August 2024")

# Work Experience
st.write("---")
st.subheader("Work Experience")
st.write("**Operations/Program Manager Intern | Hospitality Information - UCSD Sixth College**")
st.write("May 2023 - September 2024 | La Jolla, CA")
st.write(
    """
    - Led a team of 10 Clerks using agile project principles, including iterative sprints and daily stand-ups, 
    resulting in a 20% boost in productivity and enhanced team collaboration in a fast-paced environment.
    - Managed multiple tasks and deadlines, coordinating logistics for 50+ conferences using Trello and Slack, 
    improving efficiency and stakeholder satisfaction by 15%.
    - Conducted evaluations and feedback, improving database accuracy and timeliness by 15% and increasing customer 
    satisfaction by 10%.

    """
)
st.write("**Product Marketing Intern | Volition Beauty**")
st.write("May 2023 - August 2023 | San Francisco, CA")
st.write(
    """
    - Managed product roadmaps and aligned product strategy with customer needs throughout the product lifecycle, 
    contributing to a 10% expansion in brand reach and a 15% boost in engagement by integrating research findings 
    into marketing and development strategies.
    - Enhanced understanding of the product lifecycle by actively participating in product discovery, planning, and 
    development phases, driving alignment between customer experience and product strategy.
    - Created and maintained marketing databases using Salesforce, increasing email open rates by 10% and click-through 
    rates by 15%, while utilizing customer feedback to refine product features and marketing strategies, resulting in a 
    15% increase in satisfaction.
    """
)

# Leadership & Involvement
st.write("---")
st.subheader("Leadership & Involvement")
st.write("**Director of Outreach | UC San Diego Women In Business**")
st.write("November 2023 - Present | La Jolla, CA")
st.write(
    """
    - Orchestrated major events, including the Annual Business Conference with 500+ attendees, increasing sponsorships 
    by 20% and event participation by 15% through established industry partnerships that enhanced networking 
    opportunities.
    - Launched and managed the UCSD Women in Business podcast, defining the product vision, creating a content roadmap, 
    and leading market research efforts to ensure alignment with audience interests, resulting in a high-impact 
    platform for industry insights.
    - Managed event budgets, improving adherence by 10% and demonstrating strong organizational and time management skills.
    """
)

# Projects
st.write("---")
st.subheader("Projects")
st.write("**Women In Business Podcast: You Heard Her**")
st.write("Product Lead | UCSD Women In Business")
st.write(
    """
    - Defined the podcast's vision to empower and inspire women in business, developing a product strategy that positioned 
    it as a leading platform for industry insights, resulting in a 25% increase in listener engagement.
    - Created and managed a detailed roadmap for content creation and episode releases, aligning quarterly themes like 
    FinTech and product management with audience demand, which contributed to a 15% increase in listener satisfaction.
    - Conducted market research to identify trending topics and inform strategy, using feedback to iterate and enhance 
    the podcast experience.
    - Led the development and execution of campaigns, driving visibility and engagement through targeted outreach and 
    social media initiatives, achieving a 40% increase in overall podcast visibility.
    """
)