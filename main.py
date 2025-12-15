import streamlit as st
from config import OllamaConfig
from langchain_ollama import ChatOllama

model = ChatOllama(
    model=OllamaConfig.MODEL_NAME,
    base_url=OllamaConfig.BASE_URL,
    temperature=OllamaConfig.TEMPERATURE
)


st.title("🦜🔗 Quickstart App")

def generate_response(input_text):
    st.info(model.invoke(input_text))


with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "What are the three key pieces of advice for learning how to code?",
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        generate_response(text)

