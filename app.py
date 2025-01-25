import openai
import streamlit as st
import logging
import json
import requests
from PIL import Image, ImageEnhance
import base64
import time

# Configure logging
logging.basicConfig(level=logging.INFO)

# Constants
NUMBER_OF_MESSAGES_TO_DISPLAY = 20
API_DOCS_URL = "https://docs.streamlit.io/library/api-reference"

# Retrieve and validate Gemini API key (assuming the key is stored in secrets.toml file)
GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY", None)
if not GEMINI_API_KEY:
    st.error("Please add your Gemini API key to the Streamlit secrets.toml file.")
    st.stop()

# Assign Gemini API Key
headers = {"Authorization": f"Bearer {GEMINI_API_KEY}"}

# Streamlit Page Configuration
st.set_page_config(
    page_title="Math Solver AI Bot",
    page_icon="imgs/avatar_math.png",  # Replace with your desired icon
    layout="wide",
)

# Streamlit Title
st.title("AI Math Solver")


def img_to_base64(image_path):
    """Convert image to base64."""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception as e:
        logging.error(f"Error converting image to base64: {str(e)}")
        return None


@st.cache_data(show_spinner=False)
def on_chat_submit(chat_input):
    """
    Handle chat input submissions and interact with the Gemini API for solving math sums.

    Parameters:
    - chat_input (str): The math sum input from the user.

    Returns:
    - None: Updates the chat history in Streamlit's session state.
    """
    user_input = chat_input.strip().lower()

    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []

    st.session_state.conversation_history.append({"role": "user", "content": user_input})

    try:
        # API call to Gemini for solving math sum
        response = requests.post(
            "https://api.gemini.com/solve_math_sum",  # Replace with Gemini API endpoint for math sum solving
            headers=headers,
            json={"sum": user_input}
        )

        if response.status_code == 200:
            assistant_reply = response.json().get("solution", "No solution found.")
        else:
            assistant_reply = f"Error: {response.status_code}, unable to solve the sum."

        st.session_state.conversation_history.append({"role": "assistant", "content": assistant_reply})

    except requests.exceptions.RequestException as e:
        logging.error(f"Error occurred: {e}")
        st.error(f"Error: {str(e)}")


def initialize_session_state():
    """Initialize session state variables."""
    if "history" not in st.session_state:
        st.session_state.history = []
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []


def main():
    """
    Display Math Solver interface and handle the chat interface.
    """
    initialize_session_state()

    # Insert custom CSS for glowing effect
    st.markdown(
        """
        <style>
        .cover-glow {
            width: 100%;
            height: auto;
            padding: 3px;
            box-shadow: 
                0 0 5px #330000,
                0 0 10px #660000,
                0 0 15px #990000,
                0 0 20px #CC0000,
                0 0 25px #FF0000,
                0 0 30px #FF3333,
                0 0 35px #FF6666;
            position: relative;
            z-index: -1;
            border-radius: 45px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Sidebar for Mode Selection
    mode = st.sidebar.radio("Select Mode:", options=["Math Chat", "Math Updates"], index=0)

    if mode == "Math Chat":
        chat_input = st.text_input("Ask me to solve a math sum:")
        if chat_input:
            on_chat_submit(chat_input)

        # Display chat history
        for message in st.session_state.conversation_history[-NUMBER_OF_MESSAGES_TO_DISPLAY:]:
            role = message["role"]
            avatar_image = "imgs/avatar_math.png" if role == "assistant" else "imgs/user.png"
            with st.chat_message(role, avatar=avatar_image):
                st.write(message["content"])

    else:
        st.write("Stay tuned for math-related updates.")


if __name__ == "__main__":
    main()
