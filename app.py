import streamlit as st
from transformers import pipeline

# Load the summarization pipeline
@st.cache_resource  # Caching the model to load only once
def load_summarizer():
    return pipeline("summarization")

summarizer = load_summarizer()

def summarize_text(text):
    return summarizer(text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']

# Streamlit Interface
st.title("Text Summarizer")

# Text input from the user
user_input = st.text_area("Enter the text you want to summarize:")

# Display result when button is clicked
if st.button("Summarize"):
    if user_input:
        summary = summarize_text(user_input)
        st.subheader("Summary:")
        st.write(summary)
    else:
        st.warning("Please enter some text to summarize.")
