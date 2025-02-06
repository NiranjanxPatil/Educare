import streamlit as st
import google.generativeai as genai
from fpdf import FPDF

# Set up Gemini API Key
genai.configure(api_key="AIzaSyByz2fCoMLCiLP1T8e2UFlnNG96s7RlzSE")


def generate_practice_questions(topic, difficulty, num_questions):
    """
    Generate practice questions based on the selected topic, difficulty, and number of questions using the Gemini API.
    """
    prompt = f"Generate {difficulty} level math practice questions on {topic}. Provide {num_questions} questions."

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    return response.text  # Returns the generated questions as text


def evaluate_answers(questions, user_answers):
    """
    Evaluate the user's answers using the Gemini API and provide feedback.
    """
    prompt = f"Check the following answers for these math questions:\n\nQuestions:\n{questions}\n\nUser Answers:\n{user_answers}\n\nProvide correct answers and feedback."

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    return response.text  # Return AI-generated feedback


def generate_explanation(question):
    """
    Generate solution and explanation for a given question.
    """
    prompt = f"Provide the solution and a short explanation on how to solve the following math question: {question}"

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    return response.text  # Return the explanation and solution


def create_pdf(questions, file_name="questions.pdf"):
    """
    Generate a PDF containing the practice questions.
    """
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add Title
    pdf.cell(200, 10, txt="Math Practice Questions", ln=True, align='C')
    pdf.ln(10)  # Add some space between title and content

    # Add questions to PDF (Only questions, not answers or feedback)
    questions_list = questions.split("\n")
    for i, question in enumerate(questions_list[:10]):  # Limit to first 10 questions to keep the file manageable
        pdf.cell(200, 10, txt=f"Q{i + 1}: {question}", ln=True)
        pdf.ln(5)  # Add some space after each question

    # Output the PDF file
    pdf.output(file_name)
    return file_name


def practice_test():
    """
    Main function to start the practice test by selecting a topic, difficulty level,
    generating questions, getting user answers, and evaluating them.
    """
    st.title("Math Practice Test Generator")

    # Topic, Difficulty, and Number of Questions Selection
    topic = st.selectbox("Choose a math topic:", ["Algebra", "Geometry", "Calculus", "Trigonometry", "Probability"])
    difficulty = st.selectbox("Choose difficulty level:", ["Easy", "Medium", "Hard"])
    num_questions = st.number_input("Enter the number of questions:", min_value=1, max_value=20, value=5)

    # Check if questions are already generated
    if "questions" not in st.session_state:
        st.session_state["questions"] = ""
        st.session_state["answers"] = []

    if st.button("Generate Practice Questions"):
        st.write("Generating questions...")
        questions = generate_practice_questions(topic, difficulty, num_questions)

        # Store questions in session state
        st.session_state["questions"] = questions
        st.session_state["answers"] = [None] * num_questions  # Initialize answer fields

        st.write(f"### Practice Questions for {topic} ({difficulty}):")
        st.write(questions)

    # Displaying the generated questions and collecting answers
    if st.session_state["questions"]:
        question_list = st.session_state["questions"].split("\n")  # Assuming each question is on a new line
        for i, question in enumerate(question_list[:num_questions]):  # Display only the specified number of questions
            st.write(f"**Q{i + 1}:** {question}")  # Display the question
            st.session_state["answers"][i] = st.text_input(f"Your answer for Question {i + 1}:",
                                                           value=st.session_state["answers"][
                                                               i])  # Answer field below the question

        if st.button("Submit Answers"):
            st.write("Submitting answers for evaluation...")
            feedback = evaluate_answers(st.session_state["questions"], st.session_state["answers"])
            st.write("### Feedback & Evaluation:")

            # Format the feedback in a detailed manner
            feedback_lines = feedback.split("\n")  # Split feedback into lines
            question_list = st.session_state["questions"].split("\n")

            for i in range(min(len(question_list), num_questions)):
                # Get the correct answer, user answer, and feedback
                correct_answer = feedback_lines[i * 3] if i * 3 < len(feedback_lines) else "N/A"
                user_answer = st.session_state["answers"][i] if i < len(st.session_state["answers"]) else "N/A"
                is_correct = "Correct" if correct_answer == user_answer else "Incorrect"

                st.write(f"**Q{i + 1}:** {question_list[i]}")
                st.write(f"**Correct Answer:** {correct_answer}")
                st.write(f"**Your Answer:** {user_answer}")
                st.write(f"**Result:** {is_correct}")

                # Add the Expander for Solution and Explanation
                with st.expander(f"Click to view the solution and explanation for Q{i + 1}"):
                    solution = generate_explanation(question_list[i])
                    st.write(solution)
                st.write("---")

        # Button to download the questions as a PDF
        if st.button("Download Questions as PDF"):
            file_name = create_pdf(st.session_state["questions"])
            with open(file_name, "rb") as pdf_file:
                st.download_button("Download PDF", pdf_file, file_name=file_name)


# Run the Streamlit app
if __name__ == "__main__":
    practice_test()
