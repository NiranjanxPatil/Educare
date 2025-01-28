import streamlit as st
import google.generativeai as genai
import subprocess
import os

# Configure Google Generative AI
genai.configure(api_key="AIzaSyBLB6LyhnXP-dtGY1dcOVf26p1DVptYJKM")
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


def handle_error_and_retry(error_message, manim_code, attempt_count):
    """Send the error back to the API to fix and retry."""
    st.error(f"Manim error: {error_message}")
    retry_prompt = (
        f"The following Manim script failed with an error:\n"
        f"{manim_code}\n"
        f"Error message:\n{error_message}\n"
        f"Please fix the issue and return the corrected Manim script."
    )
    response = model.generate_content([retry_prompt])
    corrected_code = response.text.strip()

    # Save corrected code to file
    with open("generate_solution.py", "w") as script_file:
        script_file.write(corrected_code)

    return corrected_code, attempt_count + 1


# Solve Button
if st.button("Solve"):
    if user_input:
        try:
            # Request solution steps from Gemini
            response = model.generate_content([f"Provide step-by-step solution for: {user_input}"])
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
            # Request Python code for Manim animations with updated prompt
            prompt = (
                f"Create a Manim script that visualizes the solution for the following math problem: {user_input}.\n"
                f"Use the following guidelines strictly:\n"
                f"- All LaTeX equations must be wrapped in MathTex or Tex.\n"
                f"- Start the script with `from manim import *` and define a class inheriting from Scene.\n"
                f"- Ensure the script includes shapes, figures, and graphs where necessary.\n"
                f"- Use different colors, backgrounds, animations, and effects to enhance creativity.\n"
                f"- Add more movements and creative visuals to make the solution engaging.\n"
                f"- Avoid including any prefix or suffix like ```python or ```.\n"
                f"- Ensure the script is self-contained and does not include any additional comments or instructions.\n"
            )
            response = model.generate_content([prompt])
            manim_code = response.text.strip()

            # Save Manim code to generate_solution.py
            with open("generate_solution.py", "w") as script_file:
                script_file.write(manim_code)

            retry_limit = 2
            attempts = 0
            progress_bar = st.progress(0)  # Initialize progress bar

            while attempts < retry_limit:
                st.write(f"Retry attempt: {attempts + 1}/{retry_limit}")  # Display retry counter
                try:
                    # Update progress bar as the process starts
                    progress_bar.progress(int((attempts + 1) * 50 / retry_limit))  # 50% at the first retry

                    # Generate video using Manim
                    manim_command = ["manim", "-pql", "generate_solution.py"]
                    result = subprocess.run(manim_command, capture_output=True, text=True)

                    if result.returncode == 0:
                        # Complete progress bar after success
                        progress_bar.progress(100)
                        video_path = "media/videos/generate_solution/1080p60/Scene.mp4"  # Adjust as per Manim's output
                        if os.path.exists(video_path):
                            st.video(video_path)
                            break
                        else:
                            st.error("Video generation succeeded but video file was not found.")
                            break
                    else:
                        error_message = result.stderr
                        manim_code, attempts = handle_error_and_retry(error_message, manim_code, attempts)

                except Exception as e:
                    error_message = str(e)
                    manim_code, attempts = handle_error_and_retry(error_message, manim_code, attempts)

                # Update progress bar at each attempt
                progress_bar.progress(int((attempts + 1) * 50 / retry_limit))  # 50% at the first retry

            if attempts == retry_limit:
                st.error("Failed to generate video after 2 attempts.")

        except Exception as e:
            st.error(f"Error generating video: {e}")
