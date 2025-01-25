
import streamlit as st
import google.generativeai as genai
import subprocess
import os

# Configure Google Generative AI
genai.configure(api_key="AIzaSyByz2fCoMLCiLP1T8e2UFlnNG96s7RlzSE")
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit UI setup
st.set_page_config(page_title="Math Solution and Video Generator", layout="wide")
st.title("📚 Math Solution and Video Generator")
st.write("Enter a math equation, solve it step by step, and generate a video explanation!")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Chat history display
st.subheader("Chat History")
for chat in st.session_state["chat_history"]:
    st.markdown(f"**You:** {chat['user_input']}")
    st.markdown(f"**AI:** {chat['response']}")

# Input for math equation
st.subheader("Math Solver")
user_input = st.text_input("Enter a math equation or problem here:")

# Solve Button
if st.button("Solve"):
    if user_input:
        try:
            response = model.generate_content([user_input])
            solution_steps = response.text
            st.session_state["chat_history"].append({
                "user_input": user_input,
                "response": solution_steps,
            })
            st.markdown("### Solution Steps:")
            st.write(solution_steps)
        except Exception as e:
            st.error(f"Error solving the problem: {e}")

# Make Video Button
if st.button("Generate Video"):
    if user_input:
        try:
            # Request LaTeX code from the AI
            response = model.generate_content([f"Generate LaTeX for: {user_input}"])
            latex_code = response.text

            # Save LaTeX code to a file
            with open("latex_code.tex", "w") as latex_file:
                latex_file.write(latex_code)

            # Generate video using Manim
            manim_command = ["manim", "-pql", "generate_solution.py", "SolutionScene"]
            result = subprocess.run(manim_command, capture_output=True, text=True)

            if result.returncode == 0:
                video_path = "media/videos/generate_solution/1080p60/SolutionScene.mp4"
                if os.path.exists(video_path):
                    st.video(video_path)
                else:
                    st.error("Video generation succeeded but video file was not found.")
            else:
                st.error(f"Manim error: {result.stderr}")

        except Exception as e:
            st.error(f"Error generating video: {e}")
