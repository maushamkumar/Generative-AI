# app.py

import streamlit as st
from chatbot_logic import start_conversation, handle_user_input
from db_config import create_user_document, collection

# Initialize conversation state
if 'state' not in st.session_state:
    st.session_state.state = start_conversation()

# Streamlit app UI
st.title("Chatbot")

user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        st.session_state.state, response = handle_user_input(st.session_state.state, user_input)
        st.write(f"Chatbot: {response}")

        if st.session_state.state["step"] == "pdf" and response.startswith("Thank you"):
            user_doc = create_user_document(
                st.session_state.state["name"],
                st.session_state.state["email"],
                st.session_state.state["mobile_number"],
                st.session_state.state["pdf_filename"]
            )
            collection.insert_one(user_doc)
            st.write("Your data has been stored in the database.")
            st.session_state.state = start_conversation()  # Reset conversation
    else:
        st.write("Please enter a message.")
