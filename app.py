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

# ---------------------------
# Define Page Functions
# ---------------------------
def home_page():
    st.title("My Portfolio")
    st.write("Hi and welcome to my portfolio! I am Samuel Turner, a Level 6 Data Analyst Apprentice at Vodafone")
    
    st.subheader("About Me")
    col1, col2 = st.columns([1, 2])
    with col1:
        # Create nested columns within the left column to center the image
        left, center, right = st.columns([1, 2, 1])
        with center:
            st.image("samuel_pfp.png", width=300)
    with col2:
        st.write("""
I am Samuel Turner, 20, a Level 6 Data Analyst Apprentice at Vodafone, where I have gained 2.5 years of experience since joining the company at the age of 18. Starting my career at such a prominent organisation immediately after completing my A-Levels presented its challenges, but I embraced them with determination. I was eager to pursue further academic studies toward a degree while gaining invaluable practical experience. I firmly believe that the success of an apprenticeship is determined by the commitment of the individual, and my journey has exemplified this. I invite you to review my project portfolio to gain insight into the diverse projects I have contributed to during my apprenticeship and to appreciate the breadth of my professional skillset.
        """)
    
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
In the Gemini Chatbot Web Application Project, I developed a production-ready chatbot using Python on Vertex AI Jupyter Notebooks, despite having no prior coding experience. The application serves as an intelligent document scanner for company files by employing text vectorization for similarity searching, which enables rapid, query-based text retrieval.

For the toolchain and deployment, I utilized GitHub for source code storage and version control, while Cloud Build containerized the application through YAML configurations and Dockerfiles. The final container was then hosted on Cloud Run, secured behind a custom company DNS.

To ensure the knowledge base remained up-to-date, I established a weekly update mechanism using a Vertex AI Kubernetes pipeline. This process leveraged Beautiful Soup and the Requests library to extract HTML content from Confluence pages, with the data subsequently loaded into BigQuery.

Throughout the project, I explored the emerging capabilities of large language models (LLMs) and deepened my understanding of their functionality. Initially, I implemented a user interface using Streamlit, but later transitioned to a more flexible solution with Flask, HTML, and CSS, which required me to master new frameworks.
        """)
    
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
    st.subheader("PowerApps & PowerAutomate Tools")
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
    
    # LinkedIn contact row
    linkedin_cols = st.columns([1, 3])
    with linkedin_cols[0]:
        lottie_linkedin = load_lottieurl("https://lottie.host/c2d857da-a9fc-4986-8f61-15e77bc42c25/eUjrL2Ocmq.json")
        if lottie_linkedin:
            st_lottie(lottie_linkedin, height=200)
    with linkedin_cols[1]:
        st.markdown("### [LinkedIn Profile](https://www.linkedin.com/in/samuelturner)")
    
    # GitHub contact row
    github_cols = st.columns([1, 3])
    with github_cols[0]:
        lottie_github = load_lottieurl("https://lottie.host/94a8510d-a206-46f2-a0c5-2e34cf76437d/A3LxSpCFuF.json")
        if lottie_github:
            st_lottie(lottie_github, height=120)
    with github_cols[1]:
        st.markdown("### [GitHub Profile](https://github.com/sammysams1234)")

home_page()
