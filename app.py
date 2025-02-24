import os
import base64
import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Function to load Lottie animations from a URL
def load_lottieurl(url: str):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

# Function to encode image to Base64
def get_base64_image(image_path: str) -> str:
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Set up the page configuration
st.set_page_config(page_title="Portfolio", layout="wide", initial_sidebar_state="expanded")

def home_page():
    st.title("Samuel's Portfolio")
    st.subheader("About Me")
    
    # Two columns: one for the image, one for the bio text.
    col1, col2 = st.columns([1, 2])
    with col1:
        # Center the image using nested columns
        left, center, right = st.columns([1, 2, 1])
        with center:
            st.image("assets/samuel_pfp.png", width=500)
    with col2:
        st.write(
            """
I am Samuel Turner, 20, a Level 6 Data Analyst Apprentice at Vodafone, where I have gained 2.5 years of experience since joining the company at the age of 18. Starting my career at such a prominent organisation immediately after completing my A-Levels presented its challenges, but I embraced them with determination. I was eager to pursue further academic studies toward a degree while gaining invaluable practical experience. I firmly believe that the success of an apprenticeship is determined by the commitment of the individual, and my journey has exemplified this. I invite you to review my project portfolio to gain insight into the diverse projects I have contributed to during my apprenticeship and to appreciate the breadth of my professional skillset.
            """
        )

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
        <p>Started A-Level Education at 6th Form</p>
      </div>
      <div class="event">
        <div class="circle">2022</div>
        <p>Started Vodafone as a Data Analyst Apprentice</p>
      </div>
      <div class="event">
        <div class="circle">2025</div>
        <p>Due to graduate my Apprenticeship</p>
      </div>
    </div>
    """
    st.markdown(timeline_html, unsafe_allow_html=True)
    
    # ----------------------------------------
    # Education Section
    # ----------------------------------------
    st.markdown("---")
    st.title("Education")
    col1, col2 = st.columns([1, 2])
    with col1:
        # Ensure you have an image in your assets folder (e.g., education.png)
        st.image("assets/education.png", width=300)
    with col2:
        st.markdown(
    """
**Institution:** Denefield School  
**GCSEs:** IT, Spanish, History, Media Studies (+STEM)  
**A-Levels:** IT, Physics, Film Studies  
**Duration:** 2015 - 2022
    """
)
        st.markdown("---")
        
    col1, col2 = st.columns([1, 2])
    with col1:
        # Ensure you have an image in your assets folder (e.g., education.png)
        st.image("assets/bfc_logo.png", width=300)
    with col2:
        st.markdown(
    """
**Institution:** BlackPool & The Fylde College  
**Degree:** BSC in Digital Technology Solutions, specialising in Data and Analytics  
**Duration:** 2022 - 2025  
    """
)        

    
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
- **Chatbot Development**: Engineered a production-ready chatbot using Python on Vertex AI Jupyter Notebooks.
- **Document Scanning Tool**: Leveraged text vectorization for rapid similarity searches from company files.
- **DevOps & Deployment**: Managed version control with GitHub, containerized via Cloud Build (YAML and Dockerfiles), and deployed on Cloud Run with a custom DNS.
- **Automated Updates**: Created a weekly pipeline with Vertex AI Kubernetes, Beautiful Soup, and Requests to update BigQuery from Confluence pages.
- **UI Evolution**: Transitioned from Streamlit to a flexible Flask-based solution using HTML and CSS, while exploring LLM capabilities.        
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
- **Automated Pricing**: Developed a Python solution using Selenium and Beautiful Soup to scrape affiliate websites, structure data into tables, and store it in BigQuery—reducing labor costs and minimizing errors.
- **Process Enhancements**: Automated cleanup and organization of Confluence documentation, processed HR file data for strategic insights, and generated realistic synthetic datasets with Fakerr for testing and development.
"""
        )
    st.markdown("---")
    
    # ----------------------------------------
    # Project: Web Apps
    # ----------------------------------------
    st.subheader("Web Apps")
    col1, col2 = st.columns([1, 2])
    with col1:
        lottie_webapps = load_lottieurl("https://lottie.host/0096e542-b9df-456d-b44f-4d1d144fbde4/H4ZjV93BGj.json")
        if lottie_webapps:
            st_lottie(lottie_webapps, height=300)
    with col2:
        st.write(
"""
- **Diverse Web App Development**: Built applications using Streamlit, Flask, and React.
- **Personal Projects**: Created a Portfolio site and the Pulse Habit Tracker in Streamlit.
- **Ongoing Projects**: Currently developing Track Tracker, a music rating app utilizing Spotify's API.
- **Chatbot Development**: Experience in building web applications for a chatbot.
- **Passion for Software Development**: Strong enthusiasm for coding and development, complementing my data background.
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
- **PowerApps & Power Automate Solutions**: Developed multiple projects that streamline processes and enhance internal collaboration.
- **Skills Assessment Tool**: Built a platform for employee self-assessment and managerial ratings, with data stored in SharePoint and integrated with QlikSense for analysis.
- **Department Shadowing App**: Designed a PowerApps solution for cross-department shadowing, with Power Automate handling email confirmations and notifications.
- **Value Tracker Project**: Created an integrated solution with Jira to monitor project business value in real time, featuring a PowerApps dashboard and automated data synchronization.
"""
        )
    st.markdown("---")
    
    # ----------------------------------------
    # Personal Projects
    # ----------------------------------------
    st.title("Personal Projects")
    st.markdown("---")
    st.markdown(
        '<h3><a href="https://pulse-habit-tracker-862b964eecd4.herokuapp.com" style="color: blue; text-decoration: underline;">Pulse Habit Tracker</a></h3>',
        unsafe_allow_html=True
    )
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("assets/pulse_wireframe.png")
    with col2:
        st.write(
"""
- **Seamless Tracking**: Pulse is a state-of-the-art habit tracker built with Streamlit that offers an intuitive weekly planner and integrated to-do list—all while keeping your data secure with Google Firebase and Fernet encryption.
- **Insightful Analytics & AI Journaling**: Visual dashboards track your progress, and GPT-3.5-powered journaling delivers personalized, motivational insights.
- **Community & Growth**: Connect with peers, share progress, and enjoy a supportive environment for collective success.
"""
        )
    st.markdown("---")
    
    st.markdown(
        '<h3><a href="insert_link_here" style="color: blue; text-decoration: underline;">Track Tracker - Music Rating App</a></h3>',
        unsafe_allow_html=True
    )
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("assets/track_tracker.png")
    
    st.markdown("---")
    
    # ----------------------------------------
    # Skills Section
    # ----------------------------------------
    st.title("My Skills")
    # Inject CSS for skill images (reduced size)
    st.markdown(
        """
        <style>
        .skills-container {
            display: grid;
            grid-template-columns: repeat(4, 100px);
            gap: 1rem;
            justify-content: flex-start;
        }
        .skill-img {
            width: 100px;
            height: 100px;
            object-fit: contain;
            transition: transform 0.3s ease;
            cursor: pointer;
        }
        .skill-img:hover {
            transform: scale(1.1);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    skill_folder = "assets/skills"
    skill_images = [
        f for f in os.listdir(skill_folder)
        if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))
    ]
    skills_html = '<div class="skills-container">'
    for img_file in skill_images:
        img_path = os.path.join(skill_folder, img_file)
        img_b64 = get_base64_image(img_path)
        skills_html += f'<img class="skill-img" src="data:image/png;base64,{img_b64}" />'
    skills_html += "</div>"
    st.markdown(skills_html, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # ----------------------------------------
    # Contact Section (My Links) - Placed below Skills
    # ----------------------------------------
    st.title("My Links")
    # Inject CSS for horizontal layout of links (smaller size, left aligned)
    st.markdown(
        """
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
            flex-direction: row;
            gap: 1rem;
            align-items: center;
            justify-content: flex-start;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    linkedin_b64 = get_base64_image("assets/linkedinlogo.png")
    github_b64 = get_base64_image("assets/githublogo.png")
    pulse_b64 = get_base64_image("assets/pulselogo.png")
    
    contact_html = f"""
    <div class="contact-container">
        <a href="https://www.linkedin.com/in/samuel-turner-b6b5b0251/" target="_blank">
            <img class="clickable-img" src="data:image/png;base64,{linkedin_b64}" width="100">
        </a>
        <a href="https://github.com/sammysams1234" target="_blank">
            <img class="clickable-img" src="data:image/png;base64,{github_b64}" width="100">
        </a>
        <a href="https://pulse-habit-tracker-862b964eecd4.herokuapp.com" target="_blank">
            <img class="clickable-img" src="data:image/png;base64,{pulse_b64}" width="100">
        </a>
    </div>
    """
    st.markdown(contact_html, unsafe_allow_html=True)
    
    # ----------------------------------------
    # Contact Me Form Section (Below My Links)
    # ----------------------------------------
    st.markdown("---")
    st.title("Contact Me")
    with st.form(key='contact_form'):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button(label='Send')
        if submit_button:
            st.success("Thank you for reaching out! I will get back to you soon.")

# Run the page
home_page()
