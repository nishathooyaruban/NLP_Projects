# The ChatPromptTemplate has been moved to the main 'langchain' module.
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st


st.title("Nisha's first chatbot")

# Streamlit input text box for user queries
input_txt = st.text_input("Please enter your queries here....")

# Define the chat prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant. You are Nisha's assistant"),
        ("user", "{user_query}")
    ]
)

# Initialize the Ollama LLM with llama3
llm = Ollama(model="llama3")
output_parser = StrOutputParser()

# Create the LangChain Expression Language (LCEL) chain
chain = prompt | llm | output_parser

if input_txt:
    # Use chain.invoke() to get the response from the LLM
    response = chain.invoke({"user_query": input_txt})
    st.write(response)