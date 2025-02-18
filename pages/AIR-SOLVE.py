import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import google.generativeai as genai
from PIL import Image
import streamlit as st

st.set_page_config(layout="wide")
st.image('airsolve.png')

# Collapsible Instructions Section
with st.expander("Instructions"):
    st.write("""
       1. **Run the program** by checking the 'Run' checkbox.
       2. **Draw on the screen** using your hand gestures to create math problems.
       3. When the gesture is detected, it will be sent to the AI by showing first 4 fingers. 
       4. The **AI's answer** will appear in the chat history.
       5. **Clear the canvas** by using the 'Thumb' gesture (fist closed thumb open). 
       6. Upload images for solving math problems, and the AI will provide answers.
       """)

col1, col2 = st.columns([3, 2])
with col1:
    run = st.checkbox('Run', value=True)
    FRAME_WINDOW = st.empty()

with col2:
    st.title(" Solutions ")
    # Create a placeholder to store the chat-like responses
    chat_history = st.empty()

genai.configure(api_key="AIzaSyCYI9MmaDEv1G2QHnEfAznNwpf-FiXMofQ")
model = genai.GenerativeModel('gemini-1.5-flash')

# Initialize the webcam to capture video
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Initialize the HandDetector class with the given parameters
detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.7, minTrackCon=0.5)

prev_pos = None
canvas = None
output_texts = []  # List to hold the answers

def getHandInfo(img):
    hands, img = detector.findHands(img, draw=False, flipType=True)
    if hands:
        hand = hands[0]
        lmList = hand["lmList"]
        fingers = detector.fingersUp(hand)
        print(fingers)
        return fingers, lmList
    else:
        return None

def draw(info, prev_pos, canvas):
    fingers, lmList = info
    current_pos = None
    if fingers == [0, 1, 0, 0, 0]:
        current_pos = lmList[8][0:2]
        if prev_pos is None: prev_pos = current_pos
        cv2.line(canvas, current_pos, prev_pos, (255, 0, 255), 10)
    elif fingers == [1, 0, 0, 0, 0]:
        canvas = np.zeros_like(img)
    return current_pos, canvas

def sendToAI(model, canvas, fingers):
    if fingers == [1, 1, 1, 1, 0]:
        pil_image = Image.fromarray(canvas)
        response = model.generate_content(["Solve this math problem", pil_image])
        return response.text

while run:
    success, img = cap.read()
    if success:
        img = cv2.flip(img, 1)
        if canvas is None:
            canvas = np.zeros_like(img)
        info = getHandInfo(img)
        if info:
            fingers, lmList = info
            prev_pos, canvas = draw(info, prev_pos, canvas)
            output_text = sendToAI(model, canvas, fingers)
            if output_text:
                output_texts.append(output_text)  # Add new response to the list
                chat_history.markdown("\n\n".join(output_texts))  # Display all answers in the chat format

        image_combined = cv2.addWeighted(img, 0.7, canvas, 0.3, 0)
        FRAME_WINDOW.image(image_combined, channels="BGR")
    else:
        st.write("Failed to capture image")
else:
    cap.release()