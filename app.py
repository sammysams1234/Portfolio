import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Function to load Lottie animations from a URL
def load_lottieurl(url: str):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

# Set up the page configuration
st.set_page_config(page_title="My Portfolio", layout="wide", initial_sidebar_state="expanded")

def home_page():
    st.title("My Portfolio")
    st.write("Hi and welcome to my portfolio! I am Samuel Turner, a Level 6 Data Analyst Apprentice at Vodafone")
    
    st.subheader("About Me")
    # Two columns: one for the image, one for the bio text.
    col1, col2 = st.columns([1, 2])
    with col1:
        # Center the image using nested columns
        left, center, right = st.columns([1, 2, 1])
        with center:
            st.image("samuel_pfp.png", width=500)
    with col2:
        st.write("""
I am Samuel Turner, 20, a Level 6 Data Analyst Apprentice at Vodafone, where I have gained 2.5 years of experience since joining the company at the age of 18. Starting my career at such a prominent organisation immediately after completing my A-Levels presented its challenges, but I embraced them with determination. I was eager to pursue further academic studies toward a degree while gaining invaluable practical experience. I firmly believe that the success of an apprenticeship is determined by the commitment of the individual, and my journey has exemplified this. I invite you to review my project portfolio to gain insight into the diverse projects I have contributed to during my apprenticeship and to appreciate the breadth of my professional skillset.
        """)

    # Horizontal timeline placed below the bio
    timeline_html = """
    <style>
    .timeline {
        display: flex;
        justify-content: space-around;
        align-items: center;
        position: relative;
        margin: 20px 0;
        padding: 20px 0;
    }
    .timeline::before {
        content: "";
        position: absolute;
        top: 50%;
        left: 5%;
        right: 5%;
        height: 2px;
        background: #ddd;
        z-index: 0;
    }
    .timeline .event {
        position: relative;
        text-align: center;
        flex: 1;
        z-index: 1;
    }
    .timeline .event .circle {
        width: 20px;
        height: 20px;
        background: #FF9F55;
        border-radius: 50%;
        margin: 0 auto 10px auto;
    }
    /* Move the year up slightly */
    .timeline .event h4 {
        margin-top: -10px;
    }
    </style>
    <div class="timeline">
      <div class="event">
        <div class="circle"></div>
        <h4>2020</h4>
        <p>Started A Levels - Physics, Film Studies, IT</p>
      </div>
      <div class="event">
        <div class="circle"></div>
        <h4>2022</h4>
        <p>Started Vodafone as a Data Analyst Apprentice</p>
      </div>
      <div class="event">
        <div class="circle"></div>
        <h4>2025</h4>
        <p>Due to graduate with Digital Solutions specialising in D&A degree</p>
      </div>
    </div>
    """
    st.markdown(timeline_html, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.title("My Projects as an Apprentice")
    
    # ----------------------------------------
    # Project: E2E Gemini Document Chatbot
    # ----------------------------------------
    st.subheader("E2E Gemini Document Chatbot")
    col1, col2 = st.columns([1, 2])
    with col1:
        lottie_webapps = load_lottieurl("https://lottie.host/639148db-b5f4-4605-80b0-437e002a5038/anbsxDFgyV.json")
        if lottie_webapps:
            st_lottie(lottie_webapps, height=300)
    with col2:
        st.write("""
I engineered a production-ready chatbot using Python on Vertex AI Jupyter Notebooks, transforming a challenge into an opportunity to create a robust, intelligent document scanning tool. By leveraging text vectorization for similarity searches, the application rapidly retrieves relevant information from company files based on user queries.

Key Technical Highlights:

Version Control & Deployment: Managed source code with GitHub and utilized Cloud Build to containerize the application using YAML configurations and Dockerfiles. Successfully deployed the container on Cloud Run, secured behind a custom company DNS.
Automated Updates: Implemented a weekly update pipeline with Vertex AI Kubernetes, using Beautiful Soup and Requests to extract HTML content from Confluence pages and load the data into BigQuery. This ensures the knowledge base remains current.
UI & Framework Evolution: Initially crafted the user interface with Streamlit, then transitioned to a more flexible and scalable solution with Flask, HTML, and CSS—expanding my expertise with new frameworks.
Emerging Technologies: Explored the capabilities of large language models (LLMs) throughout the project, deepening my understanding and integration of advanced AI techniques.
This project not only showcases my ability to quickly adapt and learn new technologies but also highlights my proficiency in creating scalable, production-level applications in a dynamic, cloud-based environment.
    """
    st.markdown("---")
    
    # ----------------------------------------
    # Project: Python Automation (Pricing & Internal Processes)
    # ----------------------------------------
    st.subheader("Python Automation")
    col1, col2 = st.columns([1, 2])
    with col1:
        lottie_powerapps = load_lottieurl("https://lottie.host/db83ca77-b63f-48bf-a8c6-8f56a423f07a/OkxmUDe8EF.json")
        if lottie_powerapps:
            st_lottie(lottie_powerapps, height=300)
    with col2:
        st.write("""
In the Pricing Automation Project, I recognized that manually monitoring competitive pricing on affiliate sites was labor-intensive, error-prone, and time-consuming. To address this challenge, I developed an automated pricing solution using Python and collaborated closely with fellow developers to design and implement the system. This solution leverages Selenium and Beautiful Soup to scrape affiliate websites, transforming the extracted data into a structured, tabular format that is then stored in BigQuery. As a result, the project achieved significant labor cost savings, reduced human error, and unlocked new revenue opportunities through more informed pricing strategies.

Additionally, I implemented several internal process improvements. I developed Python-based automation scripts to clean up and organize Confluence documentation, systematically removing outdated content to maintain an accurate and efficient knowledge base. I also created ad hoc Python solutions for processing HR file data, which provided valuable insights to better position our workforce against industry consultancies. Finally, I employed the Fakerr library to generate synthetic data for testing and development, simulating realistic datasets that enhanced system robustness while ensuring data privacy.
        """)
    
    st.markdown("---")
    
    # ----------------------------------------
    # Project: PowerApps & PowerAutomate Tools
    # ----------------------------------------
    st.subheader("PowerApps & PowerAutomate Projects")
    col1, col2 = st.columns([1, 2])
    with col1:
        lottie_python = load_lottieurl("https://lottie.host/a8ca184c-72c4-4f0a-8167-f6e0546e1f7b/oBC8dtGBrA.json")
        if lottie_python:
            st_lottie(lottie_python, height=300)
    with col2:
        st.write("""
I have worked on various PowerApps/Power Automate projects that have streamlined business processes and enhanced internal collaboration.

In the Skills Assessment Tool Project, I developed a comprehensive platform that allowed employees to self-assess their skills while enabling managers to provide objective ratings. This dual-rating system streamlined the performance review process by capturing both self-perception and managerial feedback, with the data stored in SharePoint and seamlessly integrated with QlikSense for advanced analysis. Automated email notifications and reminders were implemented using Power Automate, reducing manual intervention and ensuring timely communications.

In the Department Shadowing Application Project, I designed an intuitive application that enabled employees to apply for shadowing opportunities across various departments as part of the company’s people strategy. The PowerApps-driven user interface provided a smooth and accessible application process, while Power Automate facilitated automated email confirmations and notifications, ensuring that all stakeholders remained well-informed. This project significantly enhanced cross-departmental learning and career development.

Lastly, in the Value Tracker Project, I developed a solution that integrated with Jira to monitor and track the business value of ongoing projects in real time. Built on PowerApps, the application provided a user-friendly dashboard for stakeholders to view critical project metrics, while Power Automate ensured seamless data synchronization between Jira and the tracker. This integration empowered decision-makers with timely insights, optimizing resource allocation and strategic planning.
        """)
    
    st.markdown("---")
    
    # ----------------------------------------
    # Contact Me Section
    # ----------------------------------------
    st.title("Contact Me")
    
    # Create two equal columns for contact information
    contact_cols = st.columns(1)
    with contact_cols[0]:
        st.markdown("<h3><a href='https://www.linkedin.com/in/samuel-turner-b6b5b0251/' target='_blank'>LinkedIn Profile</a></h3>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("<h3><a href='https://github.com/sammysams1234' target='_blank'>GitHub Profile</a></h3>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

home_page()
