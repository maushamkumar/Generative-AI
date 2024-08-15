# Chatbot with Streamlit, Flask, MongoDB, and WhatsApp Cloud API Integration

This project is a simple chatbot that collects user data, including name, email, mobile number, and a PDF attachment. The collected data is validated and stored in a MongoDB database. The chatbot is integrated with WhatsApp Cloud API to allow user interaction via WhatsApp, and it also features a web interface built with Streamlit.

## Features

- **Chatbot Logic**: Manages conversation flow and validates user input.
- **MongoDB Integration**: Stores user data in a MongoDB collection.
- **Streamlit Interface**: Provides a user-friendly web interface for interacting with the chatbot.
- **WhatsApp Integration**: Allows users to interact with the chatbot via WhatsApp using the WhatsApp Cloud API.
- **Flask Backend**: Handles incoming WhatsApp messages and coordinates between the chatbot and the database.

## Installation

### Prerequisites

- Python 3.8 or higher
- MongoDB Atlas or a local MongoDB instance
- WhatsApp Business API Account

### Step-by-Step Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/chatbot-project.git
   cd chatbot-project

2. ** Create and Activate Virtual Environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. ** Install Dependencies
   ```bash
   pip install -r requirements.txt
4. ** set Up Environment Variable
   ```bash
   MONGO_URI="mongodb+srv://<username>:<password>@cluster0.mongodb.net/chatbot_db?retryWrites=true&w=majority"
   WHATSAPP_ACCESS_TOKEN="YOUR_WHATSAPP_ACCESS_TOKEN"
   WHATSAPP_PHONE_NUMBER_ID="YOUR_WHATSAPP_PHONE_NUMBER_ID"
5. ** Running the Streamlit App
- In a separate terminal, you can start the Streamlit app by running:
  ```bash
  streamlit run app.py



## File Structure
- app.py: Streamlit web interface for interacting with the chatbot.
- db_config.py: MongoDB connection setup and data insertion functions.
- validation.py: Validation functions for user input.
- chatbot_logic.py: Core chatbot logic handling user interactions.
- whatsapp_api.py: Functions for sending messages via WhatsApp Cloud API.
- flask_app.py: Flask backend that processes incoming WhatsApp messages and coordinates with the chatbot logic.
- requirements.txt: Python dependencies.

## Usage
- Web Interface: Visit the Streamlit app in your browser (usually at http://localhost:8501 by default) and interact with the chatbot via the provided input field.
- WhatsApp Integration: After setting up the WhatsApp Cloud API, you can chat with the bot using your WhatsApp number. The bot will guide you through the data collection process.

### License
This project is licensed under the MIT License. See the LICENSE file for more details.

### Contributing
Feel free to submit issues and pull requests. Contributions are welcome!

### Contact
For any questions or feedback, you can contact <your-maushamkumarr26@gmail.com>


### How to Use This `README.md`:

1. **Customization**: Replace placeholder text like `"YOUR_WHATSAPP_ACCESS_TOKEN"`, `"YOUR_WHATSAPP_PHONE_NUMBER_ID"`, and any other placeholders with your actual credentials and information.

2. **Clone and Edit**: After copying the content above, paste it into a file named `README.md` in the root directory of your project. Edit any sections as needed to match your project specifics.

3. **Commit**: Add the `README.md` file to your Git repository and commit the changes:

```bash
git add README.md
git commit -m "Add README file"

.
