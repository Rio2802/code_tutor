import streamlit as st
import openai
import markdown2
from config import openai_api_key

# Set OpenAI API key
openai.api_key = openai_api_key

# Function to get response from OpenAI
def get_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use the appropriate engine
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Function to save the lesson as a Markdown file
def save_lesson(content, filename):
    with open(filename, 'w') as file:
        file.write(markdown2.markdown(content))

# Streamlit app layout
st.title("Code Tutor: AI-Powered Coding Teacher")

user_input = st.text_input("Ask Code Tutor")

if user_input:
    response = get_response(user_input)
    st.write(response)

    if st.button("Download Lesson"):
        save_lesson(response, "lesson.md")
        st.write("Lesson saved as lesson.md")
