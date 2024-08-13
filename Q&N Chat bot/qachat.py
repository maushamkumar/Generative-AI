from dotenv import load_dotenv
load_dotenv()

import streamlit as st 
import os 
import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

## Function to load Gemini Pro model and get repsonse 
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    repsonse=chat.send_message(question, stream=True) # as the LLM model is giving you the output we are going to steam it and we are going dispaly it
    return repsonse

## Initialize our streamlit app 
st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application ")

## Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = [] # To record the chat history 
    
input = st.text_input("Input: ", key='input')
sumbit = st.button("Ask the question ")

if sumbit and input:
    response = get_gemini_response(input)
    ## Add use query and response to session chat history
    st.session_state['chat_history'].append(("you", input))
    st.subheader("This Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))
        
        
st.subheader("The Chat history is ")

for role, text in st.session_state['chat_history']: # What ever is there it is either in the key-value pair 
    st.write(f"{role} : {text}")
    
    