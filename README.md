# Mental Health Chatbot

## Overview
This project is a Python Flask-based chatbot designed to support mental health and well-being by providing users with conversational support, resources, and guided interventions. The chatbot incorporates natural language understanding (NLU), context management, and response generation to deliver personalized and empathetic interactions.

---

## Features
1. **User Interface**: Interactive web interface for seamless communication.
2. **Natural Language Understanding (NLU)**: Extracts intent and emotion from user inputs.
3. **Context Management**: Maintains conversation flow and adapts responses based on context.
4. **Response Generation**: Provides meaningful and empathetic replies, including predefined and AI-generated responses.
5. **Backend Integration**: Handles request routing, session management, and system logic.

---

## Installation

### Prerequisites
- Python 3.8+
- Flask framework
- Required Python packages listed in `requirements.txt`

### Steps
1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd mental_health_chatbot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

   
## How It Works
1. **User Interaction**: Users interact with the chatbot through a web-based UI.
2. **Input Processing**: The NLU module processes user inputs to extract intent and sentiment.
3. **Context Management**: Tracks previous interactions to ensure coherent conversations.
4. **Response Generation**: Replies are generated using predefined templates or AI models.
5. **Feedback Loop**: User feedback is logged for continuous improvement.
