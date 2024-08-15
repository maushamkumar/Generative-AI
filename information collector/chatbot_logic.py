# chatbot_logic.py

from validation import is_valid_email, is_valid_mobile_number, is_valid_pdf

def start_conversation():
    return {
        "step": "name",
        "name": None,
        "email": None,
        "mobile_number": None,
        "pdf_filename": None
    }

def handle_user_input(state, user_input):
    response = ""
    
    if state["step"] == "name":
        state["name"] = user_input
        state["step"] = "email"
        response = f"Hi {user_input}, what's your email address?"

    elif state["step"] == "email":
        if is_valid_email(user_input):
            state["email"] = user_input
            state["step"] = "mobile"
            response = "Please enter your mobile number."
        else:
            response = "Invalid email format. Please enter a valid email address."

    elif state["step"] == "mobile":
        if is_valid_mobile_number(user_input):
            state["mobile_number"] = user_input
            state["step"] = "pdf"
            response = "Please upload your PDF file."
        else:
            response = "Invalid mobile number. Please enter a 10-digit number."

    elif state["step"] == "pdf":
        if is_valid_pdf(user_input):
            state["pdf_filename"] = user_input  # In a real application, handle file upload
            response = "Thank you! Your data has been submitted successfully."
        else:
            response = "Invalid PDF file. Please upload a valid PDF."

    return state, response
