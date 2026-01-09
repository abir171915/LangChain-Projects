##  Conversational Q&A ChatBot


#Importing all the dependencies
import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

#load the variables from .env file
load_dotenv()

#Accessing the key
openai_key = os.getenv("OPENAI_API_KEY")

##Streamlit UI
st.set_page_config(page_title = "Conversational Q&A ChatBot")
st.header("Hey, Let's Chat")


# Initializing ChatOpenAI
chat = ChatOpenAI(
    model = 'gpt-3.5-turbo',
    temperature= 0.6,
    api_key = openai_key
)

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content= "You are a tour guide in the UK who helps people to find out UK's most amazing tour destination and how to go there")
    ]

#Funtion to load OpenAI and get responses
def get_chatModel_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content= question))
    answer = chat.invoke(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content= answer.content))
    return answer.content

# User input box for the question
user_input = st.text_input("Input: ", key = "input")

submit = st.button("Ask the question")

# If the submit button is clicked
if submit:
    response = get_chatModel_response(user_input)

    st.subheader("The response is")
    st.write(response)

