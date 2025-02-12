import streamlit as st
from pages.home import home_page

def main():
    st.set_page_config(page_title="My Portfolio", layout="wide", initial_sidebar_state="expanded")
    home_page()

if __name__ == "__main__":
    main()
