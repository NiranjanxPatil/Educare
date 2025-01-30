import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Function for creating the header
def header():
    st.markdown("""
    <style>
        body {
            background-color: white;
        }
        .header {
            text-align: center;
            font-size: 30px;
            font-weight: bold;
            padding: 20px;
            color: #4CAF50;
            background-color: #ADD8E6;
            border-radius: 10px;
        }
        .header img {
            width: 180px;
            vertical-align: middle;
        }
    </style>
    """, unsafe_allow_html=True)

    image_path = r"C:\\projects\\temppycharm\\streamlit\\imgs\\logo.png"
    image = Image.open(image_path)

    st.markdown(
        '<div class="header"> <img src="data:image/png;base64,{}" alt="EduCare Logo"> EduCare Dashboard</div>'.format(
            image_to_base64(image)),
        unsafe_allow_html=True)

def image_to_base64(image):
    import base64
    from io import BytesIO
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Sidebar function with icons
def sidebar():
    st.sidebar.title("📌 Navigation")
    st.sidebar.markdown("Welcome to EduCare")
    st.sidebar.image(r"C:\\projects\\temppycharm\\streamlit\\imgs\\logo.png", width=50)
    options = ["🏠 Home", "📞 Contact Us", "ℹ️ About Us", "📚 Course List", "💻 Source Code & Tech"]
    selection = st.sidebar.radio("Select Option", options)
    return selection

def main_dashboard():
    st.title("🏠 Welcome to EduCare")
    st.subheader("📘 Your go-to platform for education and resources.")
    st.markdown("""
    EduCare is an online educational platform that brings together cutting-edge tech and learning resources.
    - 🎯 Interactive Courses with real-world applications.
    - 🧑‍🏫 Expert Instructors from top universities and industries.
    - 📊 Data-driven Learning Paths to track progress.
    - 🌍 Community Support & Webinars to stay updated.
    - 🔥 Career Guidance and job interview preparation.
    """)

def contact_us():
    st.title("📞 Contact Us")
    st.markdown("""Have any questions? Reach out to us.""")
    with st.form(key='contact_form'):
        name = st.text_input("👤 Name")
        email = st.text_input("📧 Email")
        message = st.text_area("💬 Your Message")
        submit_button = st.form_submit_button(label="Submit")
    if submit_button:
        st.success(f"Thank you {name}! Your message has been sent.")

def about_us():
    st.title("ℹ️ About EduCare")
    st.markdown("""
    **Our Mission**: To create a platform that bridges the gap between traditional education and modern learning.
    - 🏆 Award-winning educational platform trusted by thousands.
    - 🤖 AI-powered Personalized Learning Experiences.
    - 📚 Course materials from reputed universities & industry experts.
    - 🌟 Recognized by major tech firms for skill development.
    - 🎓 Partnerships with top institutions for certifications.
    - 🚀 Hands-on projects to enhance learning.
    - 📈 Career-oriented roadmap to help students excel.
    """)

def course_list():
    st.title("📚 Our Courses")
    st.markdown("""
    - **Web Development**: Build websites and web apps from scratch.
    - **Data Science**: Learn the fundamentals of data analytics and machine learning.
    """)

def source_code_tech():
    st.title("💻 Source Code & Tech")
    st.markdown("""
    ### Technologies Used:
    - **Python** 🐍: Core language for backend and ML tasks.
    - **Streamlit** 🚀: Fast and interactive UI development.
    - **MongoDB** 📂: NoSQL database for storing user data.
    - **Docker** 🐳: Containerized deployments for scalability.
    - **FastAPI** ⚡: Modern API framework for fast performance.
    - **TensorFlow & PyTorch** 🧠: Machine learning model integrations.
    - **AWS & GCP** ☁️: Cloud hosting and storage solutions.
    - **PostgreSQL** 🗃️: Reliable relational database support.
    - **Bootstrap & Tailwind CSS** 🎨: UI and responsive design frameworks.
    """)

def course_stats():
    st.title("📊 Course Enrollment Statistics")
    courses = ["Web Dev", "Data Science", "AI & ML", "Cloud Computing"]
    enrollments = [150, 200, 175, 120]
    fig, ax = plt.subplots()
    ax.bar(courses, enrollments, color="#2196F3")
    ax.set_xlabel("Courses")
    ax.set_ylabel("Enrollments")
    ax.set_title("Number of Enrollments per Course")
    st.pyplot(fig)

def footer():
    st.markdown("""
    <style>
        .footer {
            text-align: center;
            font-size: 12px;
            padding: 10px;
            color: white;
            background-color: #4CAF50;
            border-radius: 10px;
        }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<div class="footer">All Rights Reserved - EduCare</div>', unsafe_allow_html=True)

def main():
    header()
    option = sidebar()
    if option == "🏠 Home":
        main_dashboard()
    elif option == "📞 Contact Us":
        contact_us()
    elif option == "ℹ️ About Us":
        about_us()
    elif option == "📚 Course List":
        course_list()
    elif option == "💻 Source & Tech":
        source_code_tech()
    if option == "📚 Course List":
        course_stats()
    footer()

if __name__ == "__main__":
    main()
