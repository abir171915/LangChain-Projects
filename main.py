## Integrete code OpenAI API
import constants
import os 
from langchain_openai import OpenAI
import streamlit as st

#streamlit framework

st.title('Langchain Demon with OpenAI API')
input_text = st.text_input("Search the topic you want")

##OPENAI LLMS
llm = OpenAI(openai_api_key=constants.openai_key, temperature=0.8)



if input_text:
    response = llm.invoke(input_text)
    st.write(response)