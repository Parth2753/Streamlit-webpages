import streamlit as st
from PIL import Image

# Streamlit Page Configuration
st.set_page_config(page_title="Parth Rohilla | Profile", layout="wide")

# --- Header ---
st.title("👤 Parth Rohilla")
st.write("## AIML Enthusiast | Java & Python Learner | GitHub: Parth2753")

# --- About Section ---
st.header("About Me")
st.write(
    """
    Hi! I'm **Parth Rohilla**, passionate about **Java, Python, AIML**, and building impactful projects.
    I constantly improve my coding skills and share my work on GitHub.
    """
)

# --- Skills Section ---
st.header("Skills")
st.write(
    """
    - **Programming Languages:** Java, Python
    - **Domains:** AIML, DSA, Backend Basics
    - **Tools:** Git, Streamlit
    """
)

# --- GitHub Projects Section ---
st.header("My GitHub Projects")
st.write("Here are some highlighted repositories:")
st.markdown("- 🔗 [AI Construction Waste Management](https://github.com/Parth2753/AI-Construction-Waste-Management)")
st.markdown("- 🔗 [Java Calculator](https://github.com/Parth2753/AI-construction-waste-management)")

# --- Contact Section ---
st.header("Contact Me")
st.write("📧 Email: *parth.rohilla08@gmail.com")
st.write("📍 Location: India")


