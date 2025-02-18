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
    st.title("Personal Project - Pulse Habit Tracker")
    st.image("assets/pulse_wireframe.png")
    
    st.markdown("---")

    st.write(

    """
Pulse is an innovative and feature-rich habit tracking application designed to help users achieve personal growth and maintain consistency in their routines. Built with the powerful combination of the Python package Streamlit and the real-time database capabilities of Google Firebase, Pulse offers a secure, scalable, and easily accessible platform for individuals seeking a sustainable habit tracking solution. User data is protected with robust encryption, using Fernet encryption methods to ensure that all sensitive information is securely transmitted, offering peace of mind to users who entrust their data to the platform. At the heart of the Pulse app is its intuitive weekly planner, crafted with simplicity in mind to ensure users can effortlessly input and track their habits. Whether users aim to improve their health, increase productivity, or develop new skills, Pulse's weekly planner serves as the cornerstone for habit formation. Complementing this practical tool is an expansive analytics page that doesn’t just show a collection of stats but provides a deep, goal-specific breakdown. This empowers users to track trends and examine their progress in meaningful ways—helping users stay motivated by visually seeing their growth or discovering areas where they can improve. What sets Pulse apart from other habit trackers is its advanced AI-powered journaling feature. Using the powerful capabilities of OpenAI's GPT-3.5 model, Pulse generates dynamic and motivational summaries that offer personalized reflections on the user's habits and progress. These AI-generated insights are specifically designed to encourage users to continue refining their behaviors and enhance their commitment to their personal growth journey. Whether it's offering an encouraging reminder or suggesting areas for improvement, the journaling system provides an innovative layer of interaction that traditional habit trackers simply can’t offer. For users who value organization and simplicity, Pulse has a straightforward yet highly effective to-do list feature. This tool is designed to help users organize tasks and actions necessary to accomplish their goals, perfectly complementing the habit tracking aspects of the platform. Being organized is crucial to achieving personal success, and Pulse’s to-do list ensures that users have all their tasks and habits in one place for maximum efficiency. A unique and particularly exciting aspect of Pulse is its social element that encourages users to connect with their friends. With this feature, users can share their weekly habit progress and cheer each other on along their respective journeys. The social functionality culminates with an integrated leaderboard, introducing a fun and motivating competitive element. Friendship and friendly competition create a positive reinforcement loop, where users can strive toward completing their goals together, push each other to overcome obstacles, and celebrate their collective wins. In a world where connection and support can make all the difference in maintaining good habits, the Pulse community feature fosters camaraderie and collaboration. This aspect represents Pulse’s deeper mission of not only being about personal achievement, but also creating an encouraging environment where users can Level-up as individuals and, as a result, support the values of persistence, growth, collaboration, and shared success. Pulse is more than just an app—it's a comprehensive tool for personal transformation, to build lasting habits through continuous tracking, goal-setting, and accountability, while fostering a mindset of improvement with the assistance of AI and social engagement. for 8 seconds
Pulse is an innovative, state-of-the-art habit tracking application meticulously crafted using Streamlit to ensure an exceptionally seamless and intuitive user experience from the moment you open the app. Deeply integrated with Google Firebase's real-time database, every piece of user data is securely stored and transmitted using robust encryption protocols provided by Fernet, which means your personal information remains safe and private at all times. At the heart of Pulse lies an easy-to-navigate weekly planner that empowers users to log and monitor their daily habits effortlessly. This planner not only allows you to set and track specific goals but also serves as a dynamic tool for organizing your week in a way that promotes consistency and long-term personal growth.

Complementing the planner is a comprehensive analytics dashboard that breaks down your progress by individual goals and habits. This feature provides detailed insights and visually appealing representations of your data, helping you to pinpoint trends, measure improvement, and stay motivated as you see your achievements unfold over time. Going beyond traditional habit tracking, Pulse integrates advanced AI-powered journaling that leverages OpenAI's GPT-3.5 model. This cutting-edge feature generates personalized, motivational summaries and reflections based on your input, encouraging deeper introspection and providing fresh perspectives on your journey towards self-improvement.

In addition to these core features, Pulse includes a robust to-do list designed to enhance daily organization and productivity. This to-do list is seamlessly integrated with the habit tracking system, offering a unified view of your tasks and routines and reinforcing the app’s mission of continuous personal development. Recognizing that growth is often driven by social interaction and shared accountability, Pulse also enables you to connect with friends and peers. You can easily share your weekly habit progress, engage in friendly competitions, and even track your performance on an integrated leaderboard that fuels a spirit of community and collective achievement.

Altogether, Pulse is not just a habit tracker—it is a holistic platform that blends secure data management, insightful analytics, AI-driven journaling, and community engagement into one comprehensive tool. Whether you’re looking to establish new routines, gain valuable insights from your daily activities, or simply stay organized and motivated through social interaction, Pulse is designed to support and empower every step of your journey towards a more productive and fulfilling life."""
    
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
