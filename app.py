import streamlit as st
import openai
import os
from streamlit.components.v1 import html
from typing import List
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain import PromptTemplate
from PIL import Image

# Configuration of the app : PremAI
os.environ["OPENAI_API_KEY"] = st.secrets["openai_key"]
openai_url = st.secrets["openai_url"]
max_tokens = st.secrets["max_tokens"]

# Loading the model
llm = ChatOpenAI(openai_api_base=openai_url, max_tokens=max_tokens)

# Adding UI/UX
image = Image.open('logo.jpg')
st.set_page_config(page_title="Prem Doctor")
st.image(image, caption='')

html_temp = """
                <div style="background-color:{};padding:1px">
                
                </div>
                """

with st.sidebar:
    st.markdown("""
    # About 
    Prem Doctor is a helper tool built on [LangChain](https://langchain.com) and [PremAI](https://www.premai.io/) to analyze, detect and answer people's health questions, without exposing their information to third parties or storing it.
    """)
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
    st.markdown("""
    # How does it work
    Just write the health problem you have and wait for the answer.
    """)
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
    st.markdown("""
    Made by [Néstor Campos](https://www.linkedin.com/in/nescampos/)
    """,
    unsafe_allow_html=True,
    )

st.markdown("""
    # Prem Doctor
    """)

st.markdown("""
#### Enter the information of the disease or health problem that afflicts you, and if possible, your age or some other condition or state in order to analyze and give you a better answer. YOUR DATA IS NOT STORED, SO YOU CAN TRUST THAT THIS REMAINS BETWEEN US ;)
""")


illness = st.text_area("Describe your ailment or disease in detail to help you.", placeholder="Describe your ailment or disease in detail to help you.")

#if illness:
if st.button("Ask Prem Doctor"):
  healthhelper_template = """You are a bot that helps with health issues. 
  As an assistant, you must answer all questions related to health, solve any medical ailment or indicate the type of doctor the person should see. 
  If you don't know something, just say 'I don't currently have the information to help'. 
  Do not assume things of which you have no information.
  Question: {question}"""
  
  BOT_PROMPT = PromptTemplate(
    template=healthhelper_template, input_variables=["question"]
  )

  qa = LLMChain(llm=llm, prompt=BOT_PROMPT) 

  answer = qa.run(illness)

  st.text(f"Answer from Prem Doctor:\n\n{answer}\n\n")
