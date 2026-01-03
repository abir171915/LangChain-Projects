## Integrete code OpenAI API
import constants
import os 
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_classic.memory import ConversationBufferMemory

import streamlit as st

#1. Initialize Memory in streamlit Session State
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(memory_key="history")

#2. streamlit framework

st.title('Football Player Search Result')
input_text = st.text_input("Search the topic you want")


#3. Prompt Templates

name_prompt = PromptTemplate(
    input_variables = ["history","name"],
    template = "Tell me a summary of the player: {name}"
)

dob_prompt = PromptTemplate(
    input_variables= ["person"],
    template = "Based on the biography extract the data of birth only: {person}"
)

memorable_prompt = PromptTemplate(
    input_variables= ["dob"],
    template = "Mention two memorable events of that particular year : {dob}" 
)



#4. OPENAI LLMS
llm = OpenAI(openai_api_key=constants.openai_key, temperature=0.8)

chain = (
    # Everytime I am searching something, first I am checking is there anything in my memory
    {
        "person": (lambda x: name_prompt.format(history=st.session_state.get("memory").buffer if st.session_state.get("memory") else "",
                                                 name = x["name"]))
          | llm 
          | StrOutputParser()
          }
        | dob_prompt
        | llm
        | StrOutputParser()
        | (lambda dob_result: {"dob": dob_result})
        |memorable_prompt
        | llm
        |StrOutputParser())



if input_text:
    response = chain.invoke({"name": input_text})

    #5. Saving the interaction to the memory for NEXT run
    st.session_state.memory.save_context({"input": input_text}, {"output": response})

    st.write(response)


