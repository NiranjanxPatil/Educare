import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configure Google Generative AI
genai.configure(api_key="")
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit UI setup
st.set_page_config(page_title="AI Chatbot", layout="wide")
st.title("🤖 AI Chatbot")
st.write("Ask me anything, and I'll assist while considering the context!")

# Collapsible Instructions Section
with st.expander("Instructions"):
    st.write("""
    1. **Type your message** in the input box on the left.
    2. Click **Send** to get a response from the AI.
    3. View your **chat history** to review past interactions.
    4. **Upload an image** on the right to get AI to solve the problem.
    5. Click **Solve File** to process the uploaded image and receive the solution.
    """)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Layout: Chat history (left) and File interaction (right)
col1, col2 = st.columns([3, 1])

# Chat history section
with col1:
    st.subheader("Chat History")
    for chat in st.session_state["chat_history"]:
        st.markdown(f"**You:** {chat['user_input']}")
        st.markdown(f"**AI:** {chat['response']}")

    # Text input and send button
    st.subheader("Ask a Question")
    user_input = st.text_input("Type your message here:")
    if st.button("Send"):
        if user_input:
            response = model.generate_content([user_input])
            st.session_state["chat_history"].append({
                "user_input": user_input,
                "response": response.text,
            })
            st.experimental_rerun()

# File upload and display section
with col2:
    st.subheader("Upload Image")
    # Display the uploaded image above the upload button
    uploaded_image = st.file_uploader("Choose an image", type=['png', 'jpg', 'jpeg'])
    if uploaded_image:
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

    if st.button("Solve File"):
        if uploaded_image:
            image = Image.open(uploaded_image)
            response = model.generate_content(["Solve this math problem", image])
            st.session_state["chat_history"].append({
                "user_input": "Uploaded an image for solving.",
                "response": response.text,
            })
            st.experimental_rerun()
