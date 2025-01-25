import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Function for creating the header
def header():
    st.markdown("""
    <style>
        body {
            background-color: white;  /* Set global background to white */
        }
        .header {
            text-align: center;
            font-size: 30px;
            font-weight: bold;
            padding: 20px;
            color: #4CAF50;  /* EduCare theme color - Green */
            background-color: #ADD8E6;  /* Light Blue background */
            border-radius: 10px;  /* Rounded corners for header */
        }
        .header img {
            width: 180px;  /* Adjust logo size */
            vertical-align: middle;
        }
    </style>
    """, unsafe_allow_html=True)

    # Path to the logo image
    image_path = r"C:\projects\temppycharm\streamlit\imgs\logo.png"  # Corrected path for the logo
    image = Image.open(image_path)

    # Display the EduCare logo along with the header title
    st.markdown(
        '<div class="header"><img src="data:image/png;base64,{}" alt="EduCare Logo"> EduCare Dashboard</div>'.format(
            image_to_base64(image)),
        unsafe_allow_html=True)


def image_to_base64(image):
    import base64
    from io import BytesIO
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()


# Function for creating the sidebar with options
def sidebar():
    st.sidebar.title("Navigation")
    st.sidebar.markdown("Welcome to EduCare")

    # Sidebar background color
    st.sidebar.markdown(
        """
        <style>
            .sidebar .sidebar-content {
                background-color: #2196F3;  /* Blue background for sidebar */
                color: white;  /* White text color */
            }
            .sidebar .sidebar-content a {
                color: white;  /* Ensure links are white */
            }
            .sidebar .sidebar-content a:hover {
                color: #FFEB3B;  /* Yellow hover effect for links */
            }
        </style>
        """, unsafe_allow_html=True
    )

    # Sidebar logo/icon
    st.sidebar.image(r"C:\projects\temppycharm\streamlit\imgs\logo.png", width=50)  # Display the icon in the sidebar

    options = ["Home", "Contact Us", "About Us", "Course List", "Source Code & Tech"]
    selection = st.sidebar.radio("Select Option", options)

    return selection


# Function for creating content for the main dashboard
def main_dashboard():
    st.title("Welcome to EduCare")
    st.subheader("Your go-to platform for education and resources.")
    st.markdown("""
    EduCare is an online educational platform that brings together cutting-edge tech and learning resources. 
    Explore our content, stay updated with new courses, and become a part of the learning community.
    """)

    # New Features
    st.markdown("""
    ### New Features:
    - **Interactive Learning**: Engage in real-time courses with quizzes and feedback.
    - **Live Workshops**: Join experts in live sessions and workshops.
    - **Discussion Forums**: Connect with peers to discuss course topics and share knowledge.
    - **Progress Tracking**: Visualize your learning journey with detailed progress reports.
    """)

    # Featured Courses Carousel (Dummy data)
    st.markdown("### Featured Courses")
    st.markdown("""
    1. **Python for Data Science**: Master the fundamentals of Python and data analysis.
    2. **Web Development Bootcamp**: Learn to build modern websites with HTML, CSS, and JavaScript.
    3. **Machine Learning with AI**: Get hands-on experience with AI and machine learning models.
    """)
    st.markdown("More courses available in the Course List section.")


# Function for the "Contact Us" section
def contact_us():
    st.title("Contact Us")
    st.markdown("""
    Have any questions or need support? Reach out to us, and we will assist you.
    """)

    # Contact Form
    with st.form(key='contact_form'):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button(label="Submit")

    if submit_button:
        st.success(f"Thank you {name}! Your message has been sent.")

    # Option to download EduCare brochure
    st.markdown("[Download EduCare Brochure](https://via.placeholder.com/150)")


# Function for the "About Us" section with Testimonials
def about_us():
    st.title("About EduCare")
    st.markdown("""
    EduCare is dedicated to providing the best educational resources, cutting-edge tools, and learning experiences. 
    We aim to empower learners around the world by combining technology with education. 

    **Our Mission**: To create a platform that bridges the gap between traditional education and modern, interactive learning.

    **Our Vision**: EduCare envisions a world where education is accessible, engaging, and empowering for all.

    **Meet the Team**:
    - **John Doe**: Co-Founder & CEO
    - **Jane Smith**: Head of Content and Strategy
    - **Samuel Lee**: CTO - Tech Lead

    ### What Our Users Say:
    - "EduCare is an amazing platform! The courses are well-structured, and the community is very supportive."
    - **John Doe**, Software Developer

    - "I learned a lot about data science and AI through EduCare. The resources and guides were extremely helpful!"
    - **Jane Smith**, Data Scientist

    - "Thanks to EduCare, I was able to take my skills to the next level. The interactive content made learning enjoyable!"
    - **Samuel Lee**, Web Developer
    """)

    # Embed a video or image (example)
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")


# Function for the "Course List" section
def course_list():
    st.title("Our Courses")
    st.markdown("""
    We offer a variety of courses in areas such as:
    - **Web Development**: Build websites and web apps from scratch.
    - **Data Science**: Learn the fundamentals of data analytics and machine learning.
    - **AI & Machine Learning**: Explore cutting-edge technologies and tools.
    - **Cloud Computing**: Gain hands-on experience with cloud platforms.
    """)

    st.markdown("""
    ### Filter Courses by Category:
    - Beginner
    - Intermediate
    - Advanced
    """)

    # Display detailed course information
    st.markdown("""
    #### Python for Data Science (Beginner):
    - Duration: 3 months
    - Overview: Learn Python programming and data analysis techniques.
    - Difficulty: Easy
    - Enroll Now: [Link to Course]
    """)

    st.markdown("""
    #### Web Development Bootcamp (Intermediate):
    - Duration: 4 months
    - Overview: Master HTML, CSS, and JavaScript to create modern websites.
    - Difficulty: Medium
    - Enroll Now: [Link to Course]
    """)


# Function for the "Source Code & Tech We Used" section
def source_code_tech():
    st.title("Source Code & Tech")
    st.markdown("""
    ### Source Code:
    The source code is available on our GitHub repository. Feel free to explore and contribute to the project!
    [GitHub Link](https://github.com/educare)

    ### Technologies Used:
    - **Python**: For backend processing and logic.
    - **Streamlit**: For building interactive UIs.
    - **MongoDB**: For database management.
    - **Docker**: For containerization and environment consistency.
    - **AWS**: For cloud hosting and services.
    """)


# Function for plotting a sample graph (e.g., course statistics)
def course_stats():
    st.title("Course Enrollment Statistics")
    # Sample data for illustration
    courses = ["Web Development", "Data Science", "AI & ML", "Cloud Computing"]
    enrollments = [150, 200, 175, 120]

    # Plotting the bar chart
    fig, ax = plt.subplots()
    ax.bar(courses, enrollments, color="#2196F3")
    ax.set_xlabel("Courses")
    ax.set_ylabel("Enrollments")
    ax.set_title("Number of Enrollments per Course")

    st.pyplot(fig)


# Function for creating footer with watermark
def footer():
    st.markdown("""
    <style>
        .footer {
            text-align: center;
            font-size: 12px;
            padding: 10px;
            color: white;  /* White text for footer */
            background-color: #4CAF50;  /* EduCare theme color - Green */
            border-radius: 10px;  /* Rounded corners for footer */
        }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<div class="footer">All Rights Reserved - EduCare</div>', unsafe_allow_html=True)


# Main UI flow
def main():
    # Place header at the top
    header()

    # Main content area
    option = sidebar()

    if option == "Home":
        main_dashboard()
    elif option == "Contact Us":
        contact_us()
    elif option == "About Us":
        about_us()
    elif option == "Course List":
        course_list()
    elif option == "Source Code & Tech":
        source_code_tech()

    # Display course statistics
    if option == "Course List":
        course_stats()

    # Place footer at the bottom
    footer()


if __name__ == "__main__":
    main()
