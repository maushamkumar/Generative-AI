from dotenv import load_dotenv
load_dotenv() # Loading all the environment variables 

import streamlit as st 
import os 
import google.generativeai as genai 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Gemini pro model get repsonses 
model=genai.GenerativeModel() # For vision use Geminiprovision 
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text


# ## Initialize our streamlit app 

# st.set_page_config(page_title='Q&A Demo')

# st.header("Gemini LLM Application")

# input=st.text_input('Input: ', key="input")
# submit = st.button("Ask the question")

# # When submit is clicked 
# if submit:
#     response=get_gemini_response(input)
#     st.subheader("The Response is ")
#     st.write(response)




# Function to simulate a response from a model
# def generate_response(user_input):
    # This is a placeholder for the actual model response
    # Replace this with your model's prediction logic
    # return f"Response to: {user_input}"
# Title of the application


from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Initialize conversation history
conversation = []

# Simulated AI response function (replace this with your actual AI model call)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_message = request.form['message']
        conversation.append({'sender': 'You', 'text': user_message, 'type': 'user'})
        
        ai_response = get_gemini_response(user_message)
        conversation.append({'sender': 'AI', 'text': ai_response, 'type': 'ai'})
        
        return redirect(url_for('index'))

    return render_template('index.html', conversation=conversation)

@app.route('/send', methods=['POST'])
def send():
    user_message = request.form['message']
    conversation.append({'sender': 'You', 'text': user_message, 'type': 'user'})
    
    ai_response = get_gemini_response(user_message)
    conversation.append({'sender': 'AI', 'text': ai_response, 'type': 'ai'})
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)