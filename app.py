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
    st.subheader("About Me")
    # Two columns: one for the image, one for the bio text.
    col1, col2 = st.columns([1, 2])
    with col1:
        # Center the image using nested columns
        left, center, right = st.columns([1, 2, 1])
        with center:
            st.image("assets/samuel_pfp.png", width=500)
    with col2:
        st.write("""
I am Samuel Turner, 20, a Level 6 Data Analyst Apprentice at Vodafone, where I have gained 2.5 years of experience since joining the company at the age of 18. Starting my career at such a prominent organisation immediately after completing my A-Levels presented its challenges, but I embraced them with determination. I was eager to pursue further academic studies toward a degree while gaining invaluable practical experience. I firmly believe that the success of an apprenticeship is determined by the commitment of the individual, and my journey has exemplified this. I invite you to review my project portfolio to gain insight into the diverse projects I have contributed to during my apprenticeship and to appreciate the breadth of my professional skillset.
        """)

    # Horizontal animated timeline placed below the bio
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
/* Animate the connecting line */
.timeline::before {
    content: "";
    position: absolute;
    top: 50%;
    left: 5%;
    right: 5%;
    height: 2px;
    background: #ddd;
    z-index: 0;
    animation: drawLine 1s forwards;
}

@keyframes drawLine {
    from { transform: scaleX(0); }
    to { transform: scaleX(1); }
}

.timeline .event {
    position: relative;
    text-align: center;
    flex: 1;
    z-index: 1;
    opacity: 0;
    transform: translateY(20px);
    animation: slideIn 0.5s forwards;
}

/* Stagger the animation for each event */
.timeline .event:nth-child(1) { animation-delay: 1s; }
.timeline .event:nth-child(2) { animation-delay: 2s; }
.timeline .event:nth-child(3) { animation-delay: 3s; }

@keyframes slideIn {
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Style the circle as a container for the year */
.timeline .event .circle {
    width: 40px;
    height: 40px;
    background: #E60000;
    border-radius: 50%;
    margin: 0 auto 10px auto;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 14px;
    font-weight: bold;
    opacity: 0;
    transform: scale(0);
    animation: popIn 0.5s forwards;
}

/* Stagger the circle animations to match their parent event */
.timeline .event:nth-child(1) .circle { animation-delay: 0.3s; }
.timeline .event:nth-child(2) .circle { animation-delay: 0.6s; }
.timeline .event:nth-child(3) .circle { animation-delay: 0.9s; }

@keyframes popIn {
    to {
        opacity: 1;
        transform: scale(1);
    }
}
</style>

<div class="timeline">
  <div class="event">
    <div class="circle">2020</div>
    <p>Started A Levels - Physics, Film Studies, IT</p>
  </div>
  <div class="event">
    <div class="circle">2022</div>
    <p>Started Vodafone as a Data Analyst Apprentice</p>
  </div>
  <div class="event">
    <div class="circle">2025</div>
    <p>Due to graduate with Digital Solutions specialising in D&amp;A degree</p>
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
        st.write(
    """
    I engineered a production-ready chatbot using Python on Vertex AI Jupyter Notebooks, transforming a challenge into an opportunity to create a robust, intelligent document scanning tool. By leveraging text vectorization for similarity searches, the application rapidly retrieves relevant information from company files based on user queries. I managed version control with GitHub, utilized Cloud Build for containerizing the application with YAML configurations and Dockerfiles, and deployed it on Cloud Run secured behind a custom company DNS. Furthermore, I implemented a weekly update pipeline with Vertex AI Kubernetes that employs Beautiful Soup and Requests to extract HTML content from Confluence pages and load the data into BigQuery, ensuring that the knowledge base remains current. The project also saw an evolution in UI frameworks, starting with Streamlit and transitioning to a more flexible solution with Flask, HTML, and CSS, all while exploring the emerging capabilities of large language models (LLMs).
    """
                )
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
        st.write(
    """
    I developed a suite of solutions under the Pricing Automation & Process Enhancements portfolio that significantly streamlined business operations. First, I engineered an automated pricing solution using Python, which leverages Selenium and Beautiful Soup to scrape affiliate websites, structure the extracted data into a tabular format, and store it in BigQuery. This approach drastically reduced labor costs, minimized human errors, and unlocked new revenue opportunities through more informed pricing strategies. In addition, I created separate projects to further enhance internal processes: one involved developing Python scripts to automate the cleanup and organization of Confluence documentation, ensuring an up-to-date knowledge base; another focused on processing HR file data to deliver strategic insights for workforce optimization; and a third employed the Fakerr library to generate realistic synthetic datasets for testing and development, thereby enhancing system robustness while ensuring data privacy.
    """
                )
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
        st.write(
    """
    I have developed a series of PowerApps and Power Automate projects that have streamlined business processes and enhanced internal collaboration. In the Skills Assessment Tool Project, I built a comprehensive platform that enabled employees to self-assess their skills while managers provided objective ratings, effectively streamlining performance reviews by capturing both self-perception and managerial feedback, with data stored in SharePoint and integrated with QlikSense for advanced analysis. In the Department Shadowing Application Project, I designed an intuitive PowerApps-driven solution that facilitated cross-departmental shadowing opportunities as part of the company’s people strategy, with Power Automate handling automated email confirmations and notifications to keep all stakeholders informed. Lastly, in the Value Tracker Project, I developed an integrated solution with Jira that monitors and tracks the business value of ongoing projects in real time, offering a user-friendly dashboard built on PowerApps and leveraging Power Automate for seamless data synchronization, thereby empowering decision-makers with timely insights for optimized resource allocation and strategic planning.
    """
        )
    
    st.markdown("---")
    
    # ----------------------------------------
    # Contact Me Section with Clickable Animated Images
    # ----------------------------------------
    st.title("Contact Me")
    
    # CSS for clickable image animation
    st.markdown("""
    <style>
    .clickable-img {
        transition: transform 0.3s ease;
        cursor: pointer;
    }
    .clickable-img:hover {
        transform: scale(1.1);
    }
    .contact-container {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Display the clickable images
    st.markdown("""
    <div class="contact-container">
        <a href="https://www.linkedin.com/in/samuel-turner-b6b5b0251/" target="_blank">
            <img class="clickable-img" src="assets/linkedinlogo.png" width="150">
        </a>
        <a href="https://github.com/sammysams1234" target="_blank">
            <img class="clickable-img" src="assets/githublogo.png" width="150">
        </a>
    </div>
    """, unsafe_allow_html=True)

home_page()
