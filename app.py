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
st.set_page_config(page_title="My Awesome Portfolio", layout="wide", initial_sidebar_state="expanded")

# ---------------------------
# Define Page Functions
# ---------------------------

def projects_page():
    st.title("Projects")
    st.write("Below are a few projects that showcase my skills and passion for creating amazing digital products.")
    
    # ----------------------------------------
    # Project: Web Apps
    # ----------------------------------------
    st.subheader("Web Apps Development")
    col1, col2 = st.columns([1, 2])
    with col1:
        lottie_webapps = load_lottieurl("https://lottie.host/0096e542-b9df-456d-b44f-4d1d144fbde4/H4ZjV93BGj.json")
        if lottie_webapps:
            st_lottie(lottie_webapps, height=300)
    with col2:
        st.write("""
        **Description:**  
        A portfolio of web applications that demonstrate a range of web development skills using modern frameworks and responsive design principles.
        """)
    st.markdown("---")
    
    # ----------------------------------------
    # Project: PowerApps
    # ----------------------------------------
    st.subheader("Project: PowerApps")
    col1, col2 = st.columns([1, 2])
    with col1:
        lottie_powerapps = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_3rwasyjy.json")
        if lottie_powerapps:
            st_lottie(lottie_powerapps, height=300)
    with col2:
        st.write("""
        **Description:**  
        Developed interactive business applications using PowerApps to streamline processes, improve collaboration, and drive efficiency.
        """)
    st.markdown("---")
    
    # ----------------------------------------
    # Project: Python Automation
    # ----------------------------------------
    st.subheader("Project: Python Automation")
    col1, col2 = st.columns([1, 2])
    with col1:
        lottie_python = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_x62chJ.json")
        if lottie_python:
            st_lottie(lottie_python, height=300)
    with col2:
        st.write("""
        **Description:**  
        Automated repetitive tasks using Python, resulting in increased efficiency and reduced errors. This project showcases my ability to create robust automation scripts.
        """)
# ---------------------------
# Sidebar Navigation
# ---------------------------

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Projects"))

if page == "Projects":
    projects_page()

