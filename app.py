# Q&A Chatbot

from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()   #take environment variables from .env.

import streamlit as st
import os
## Function to load openai model and get response

def get_openai_response(question):
    llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"),temperature=0.6,model_name="gpt-3.5-turbo-instruct")
    response = llm(question)
    return response

## initialize our streamlit app

st.set_page_config(page_title="Q&A Chatbot", page_icon=":robot:")

st.header("Langchain Q&A Chatbot")

input = st.text_input("Input: ", key='input')
response = get_openai_response(input)

submit = st.button("Ask a question")

## if ask button clicked

if submit:
    st.subheader("The answer is:")
    st.write(response)