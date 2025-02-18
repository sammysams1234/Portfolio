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
I have developed web applications using Streamlit, Flask and React at a basic level. Many have been personal projects - like this Portfolio site! I have also developed an application in Streamlit called Pulse Habit Tracker which allows users to track habits, manage an AI-Powered well-being journal, and a friend system for habit leaderboards. In addition, a music rating app called Track Tracker is in the works utilising Spotify's API capabilities.
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
I have developed a series of PowerApps and Power Automate projects that have streamlined business processes and enhanced internal collaboration. In the Skills Assessment Tool Project, I built a comprehensive platform that enabled employees to self-assess their skills while managers provided objective ratings, effectively streamlining performance reviews by capturing both self-perception and managerial feedback, with data stored in SharePoint and integrated with QlikSense for advanced analysis. In the Department Shadowing Application Project, I designed an intuitive PowerApps-driven solution that facilitated cross-departmental shadowing opportunities as part of the company's people strategy, with Power Automate handling automated email confirmations and notifications to keep all stakeholders informed. Lastly, in the Value Tracker Project, I developed an integrated solution with Jira that monitors and tracks the business value of ongoing projects in real time, offering a user-friendly dashboard built on PowerApps and leveraging Power Automate for seamless data synchronization, thereby empowering decision-makers with timely insights for optimized resource allocation and strategic planning.
            """
        )
    st.markdown("---")
    
    # ----------------------------------------
    # Personal Project: Pulse Habit Tracker
    # ----------------------------------------
    st.markdown(
    '<h1>Personal Project - <a href="https://pulse-habit-tracker-862b964eecd4.herokuapp.com" style="color: blue; text-decoration: underline;">Pulse Habit Tracker</a></h1>',
    unsafe_allow_html=True
    )


    st.image("assets/pulse_wireframe.png")
    
    st.markdown("---")

    st.subheader("Pulse Features")

    st.write(
    """
- **Seamless and Intuitive Experience**: Pulse is a state-of-the-art habit tracking application built using Streamlit, designed to deliver an exceptionally seamless and user-friendly experience from the very first interaction.
- **Robust Security & Data Management**: Deeply integrated with Google Firebase's real-time database, every piece of user data is securely stored and transmitted using robust encryption protocols via Fernet, ensuring complete data safety and privacy.
- **Dynamic Weekly Planner**: At the heart of Pulse is an easy-to-navigate weekly planner that empowers users to log and monitor their daily habits. This planner not only lets you set and track specific goals but also serves as a dynamic organizational tool to promote consistency and long-term personal growth.
- **Comprehensive Analytics Dashboard**: Pulse features a detailed analytics dashboard that breaks down your progress by individual goals and habits. This visual representation helps identify trends, measure improvements, and keep you motivated as you watch your achievements unfold over time.
- **Advanced AI-Powered Journaling**: Leveraging OpenAI's GPT-3.5 model, the app offers AI-powered journaling that generates personalized, motivational summaries and reflective insights. This feature encourages deeper introspection and provides fresh perspectives to enhance your self-improvement journey.
- **Integrated To-Do List**: The robust to-do list is seamlessly integrated into the app, enhancing your daily organization and productivity. It reinforces the platform’s mission of continuous personal development by ensuring that all your tasks align with your habit tracking and growth objectives.
- **Community Engagement & Social Features**: Pulse goes beyond individual tracking by allowing users to connect with friends and peers. Share your weekly progress, engage in friendly competition via an integrated leaderboard, and experience the motivation of a supportive community striving for collective success.
- **Holistic Self-Improvement Platform**: Combining secure data management, insightful analytics, AI-driven journaling, and community engagement, Pulse is more than just a habit tracker. It’s a comprehensive tool designed to empower you on every step of your journey towards a more productive, fulfilling, and balanced life.
    """
    )

    st.markdown("---")
    
    col_left, col_right = st.columns(2)
    
    # Skills Section
    with col_left:
        st.title("My Skills")
        # Inject CSS for skill images
        st.markdown(
            """
            <style>
            .skills-container {
                display: grid;
                grid-template-columns: repeat(4, 150px);
                gap: 2rem;
                justify-content: flex-start;
            }
            .skill-img {
                width: 150px;
                height: 150px;
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
    
    # Contact Section
    with col_right:
        st.title("My Links")
        # Inject CSS for horizontal layout of links
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
                gap: 2rem;
                align-items: center;
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
                <img class="clickable-img" src="data:image/png;base64,{linkedin_b64}" width="150">
            </a>
            <a href="https://github.com/sammysams1234" target="_blank">
                <img class="clickable-img" src="data:image/png;base64,{github_b64}" width="150">
            </a>
            <a href="https://pulse-habit-tracker-862b964eecd4.herokuapp.com" target="_blank">
                <img class="clickable-img" src="data:image/png;base64,{pulse_b64}" width="150">
            </a>
        </div>
        """
        st.markdown(contact_html, unsafe_allow_html=True)

# Run the page
home_page()
