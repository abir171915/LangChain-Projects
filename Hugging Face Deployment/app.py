# Q&A ChatBot
import constants
from constants import openai_key
from langchain_openai import ChatOpenAI
import streamlit as st


## Function load OpenAI model and get the responses

def get_openai_response(question):
    llm = ChatOpenAI(
        model = 'gpt-4o-mini',
        temperature= 0.6,
        api_key= openai_key
    )
    response = llm.invoke(question)
    return response.content

## Initialize Streamlit app

st.set_page_config(page_title= "Q&A ChatBot")
st.header("Langchain Application")

# User input box for the question
user_input = st.text_input("Input: ", key = "input")

submit = st.button("Ask the question")

# If the submit button is clicked
if submit:
    response = get_openai_response(user_input)

    st.subheader("The response is")
    st.write(response)



