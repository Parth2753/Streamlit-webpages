import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Parth Rohilla | Portfolio", page_icon="💼", layout="wide")

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://mail.google.com/mail/u/0?ui=2&ik=a0717bdfea&attid=0.1&permmsgid=msg-a:r-6578503620898569299&th=19ab030ccd13797e&view=att&disp=safe&realattid=19ab030bd27909592ae1&zw", width=200)  # Replace with your photo URL
    st.title("Parth Rohilla")
    st.markdown("**Aspiring Developer | Python & Java Enthusiast**")
    st.markdown("---")
    st.markdown("📍 India")
    st.markdown("[📧 Email Me](mailto:parth.rohilla08@gmail.com)")
    st.markdown("[🌐 LinkedIn](https://www.linkedin.com/in/parth-rohilla-b14919361/)")
    st.markdown("[💻 GitHub](https://github.com/Parth2753")
    st.markdown("---")
    st.write("© 2025 Parth Rohilla")

# --- MAIN PAGE ---
st.markdown("<h1 style='text-align:center; color:#4B8BBE;'>Welcome to My Portfolio 💼</h1>", unsafe_allow_html=True)
st.write("")

# --- ABOUT SECTION ---
st.header("👨‍💻 About Me")
st.write("""
Hello! I'm **Parth Rohilla**, a passionate learner exploring the world of **programming and technology**.  
I enjoy solving logical problems, writing clean code, and constantly improving my skills.
My goal is to become a ai developer full-stack developer and create impactful digital solutions.
""")

# --- SKILLS SECTION ---
st.header("🧠 Skills")
cols = st.columns(5)
skills = ["Python", "Java", "Git & GitHub", "HTML/CSS", "Streamlit"]
for i, skill in enumerate(skills):
    with cols[i]:
        st.button(skill)

# --- PROJECTS SECTION ---
st.header("🚀 Projects")

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📱 Calculator App")
        st.write("A simple **Java calculator** using command-line interface.")
        st.markdown("[🔗 View on GitHub](https://github.com/Parth2753/)")
    with col2:
        st.subheader("AI Constrcution Waste Management")
        st.write("A program used to check the registration of waste collected each day ")
        st.markdown("[🔗 View on GitHub](https://github.com/Parth2753)")

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🌐 Streamlit Portfolio")
        st.write("This interactive portfolio built using **Streamlit** with Python.")
        st.markdown("[🔗 View on GitHub](https://github.com/Parth2753)")
    with col2:
        st.subheader("🎮 Mini Projects")
        st.write("A collection of small, fun programs made while learning coding.")
        st.markdown("[🔗 View on GitHub](https://github.com/Parth2753)")

# --- EDUCATION SECTION ---
st.header("🎓 Education")
st.write("""
- **High School Student**, Focused on *Maths, Physics, and Chemistry*  
- Learning **Python**, **Java**, and **Software Development Concepts**
""")

# --- CONTACT SECTION ---
st.header("📫 Get in Touch")
contact_form = """
<form action="https://formsubmit.co/your_email@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send ✉️</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

# --- CUSTOM CSS ---
st.markdown("""
<style>
/* General styling */
body { background-color: #f9f9f9; color: #333; }

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #1E1E1E;
    color: white;
    padding: 2rem 1rem;
}

/* Buttons */
button[kind="secondary"] {
    border-radius: 8px !important;
    background-color: #4B8BBE !important;
    color: white !important;
}

/* Contact form */
input, textarea {
    width: 100%;
    padding: 0.6rem;
    margin-bottom: 0.6rem;
    border: 1px solid #ccc;
    border-radius: 5px;
}
button[type="submit"] {
    background-color: #4B8BBE;
    color: white;
    padding: 0.6rem 1.2rem;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}
button[type="submit"]:hover {
    background-color: #306998;
}
</style>
""", unsafe_allow_html=True)


