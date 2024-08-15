# flask_app.py

from flask import Flask, request, jsonify
from whatsapp_api import send_whatsapp_message
from db_config import create_user_document, collection
from chatbot_logic import start_conversation, handle_user_input

app = Flask(__name__)

user_states = {}

def get_user_state(phone_number):
    if phone_number not in user_states:
        user_states[phone_number] = start_conversation()
    return user_states[phone_number]

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    phone_number = data['entry'][0]['changes'][0]['value']['messages'][0]['from']
    message_text = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']

    user_state = get_user_state(phone_number)

    user_state, response = handle_user_input(user_state, message_text)

    send_whatsapp_message(phone_number, response)

    if user_state["step"] == "pdf" and response.startswith("Thank you"):
        user_doc = create_user_document(
            user_state["name"],
            user_state["email"],
            user_state["mobile_number"],
            user_state["pdf_filename"]
        )
        collection.insert_one(user_doc)
        user_states.pop(phone_number)  # End conversation

    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
