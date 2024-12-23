from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import random

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

# Updated responses with emojis and actionable tips
responses = {
    "greeting": [
        "Hello! 😊 I'm here to support you. How are you feeling today?",
        "Hi there! 👋 Let's talk. How can I help you today?",
        "Hello! 💬 Remember, it's okay to seek help. How are you?"
    ],
    "feeling_good": [
        "That's wonderful to hear! 🎉 Keep cherishing those positive moments.",
        "I'm glad you're feeling good. 😊 Remember to celebrate small victories!",
        "Great! 🌟 Staying positive is a key part of mental well-being. What made you feel good today?"
    ],
    "feeling_down": [
        "I'm sorry to hear that. 😔 It's okay to have tough days. Would you like some tips?",
        "It's perfectly okay to feel this way. 💙 I'm here to listen. Want to share more?",
        "Remember, you're not alone. 🌈 Take a deep breath, and let me know how I can help."
    ],
    "anger": [
        "It's okay to feel angry sometimes. 😡 Taking deep breaths can help calm your mind.",
        "Try to express your anger in a healthy way, like writing it down or talking to someone you trust. ✍️",
        "Consider stepping away from the situation and returning once you feel calmer. 🌿",
        "Would you like some advice on managing anger better? 🧘"
    ],
    "dizzy": [
        "If you're feeling dizzy, try sitting or lying down immediately to avoid falling. ⚠️",
        "Drink some water—it might help if you're dehydrated. 💧",
        "Avoid sudden movements and take slow, deep breaths. 🌬️ If it persists, consider seeking medical help.",
        "Would you like more tips on managing dizziness? 🩺"
    ],
    "anxiety": [
        "Anxiety can be tough. 😟 Try grounding exercises, like naming five things you see around you. 👀",
        "Breathing techniques can help. 🌬️ Inhale for 4 seconds, hold for 4, and exhale for 6 seconds.",
        "Remember, anxiety is temporary. ⏳ It will pass. Would you like to talk more about it? 🗣️"
    ],
    "fatigue": [
        "Fatigue can be overwhelming. 😴 Try taking short breaks and drinking water. 💦",
        "Are you getting enough sleep? 🛏️ Rest is essential for your body and mind.",
        "If possible, take a power nap or stretch to recharge yourself. 🧘‍♂️",
        "Consider light physical activity—it can help fight fatigue. 🏃‍♀️"
    ],
    "confusion": [
        "It's okay to feel confused. 🤔 Take a deep breath and give yourself time to process. 🧘‍♂️",
        "Sometimes writing things down can help organize your thoughts. 📝",
        "Break the problem into smaller steps and focus on one at a time. 📋",
        "Would you like to talk about what's confusing you? 💬"
    ],
    "relationship": [
        "Communication is key. 💬 Talk openly and honestly with your partner about your feelings. 👫",
        "Every relationship has ups and downs. 🌈 Focus on understanding each other instead of trying to 'win' arguments.",
        "Set boundaries and respect each other's space and time. ⏳",
        "Show appreciation for your partner regularly, even with small gestures like a 'thank you' or a compliment. 💖",
        "Be patient and willing to work together to solve issues. Relationships require teamwork. 🤝"
    ],
    "advice": [
        "Take a moment to breathe deeply. 🌬️ Try inhaling for 4 seconds, holding for 7, and exhaling for 8.",
        "Consider taking a short walk or doing a light stretch to clear your mind. 🚶‍♀️",
        "Write down three things you're grateful for today. ✨ It can make a difference!",
        "Reach out to a friend or family member and talk about how you're feeling. 🤝",
        "Try to practice mindfulness by focusing on your breathing for a few minutes. 🧘‍♀️"
    ],
    "tips": [
        "Here are some general tips to improve your well-being: 🌟\n"
        "- Take short breaks during work to refresh your mind. ⏸️\n"
        "- Practice gratitude—write down three things you're grateful for today. ✨\n"
        "- Stay hydrated and eat balanced meals. 🥗\n"
        "- Engage in regular physical activity. Even a 10-minute walk helps. 🚶‍♀️\n"
        "- Maintain a consistent sleep schedule for better rest. 🛏️",
        
        "If you're feeling overwhelmed: 😟\n"
        "- Pause for a moment and take deep breaths. Inhale for 4 seconds, hold for 7, exhale for 8. 🌬️\n"
        "- Break your tasks into smaller, manageable steps. 📋\n"
        "- Reach out to a friend or family member for support. 🤝",
        
        "For improving focus and productivity: 🎯\n"
        "- Use the Pomodoro technique: work for 25 minutes, then take a 5-minute break. ⏲️\n"
        "- Eliminate distractions by turning off unnecessary notifications. 📵\n"
        "- Organize your tasks with a to-do list or planner. 📝"
    ],
    "thank_you": [
        "You're welcome! 😊 I'm glad I could help.",
        "No problem at all! 🌟 Let me know if there's anything else you need.",
        "It's my pleasure to help you. Take care! 🌱",
        "You're very welcome! Remember, I'm always here if you need me. 💙"
    ],
    "ok": [
        "Got it! 👍 Let me know if there's anything else you need.",
        "Okay! 😊 Feel free to share more if you'd like.",
        "Alright! 🌟 I'm here to help with anything else.",
        "Sure thing! 💬 Let me know how I can assist further."
    ],
    "default": [
        "I'm here to help. 😊 Can you tell me more about what's on your mind?",
        "Feel free to share anything you're comfortable with. 🤗 I'm here to listen.",
        "You can talk to me about anything. 🌟 I'm here to support you."
    ]
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-response", methods=["POST"])
def get_response():
    data = request.get_json()
    user_message = data.get("message", "").lower()

    if not user_message:
        return jsonify({"error": "Message is required!"}), 400

    # Enhanced keyword-based logic with emoji responses
    if any(word in user_message for word in ["hi", "hello", "hey"]):
        bot_message = random.choice(responses["greeting"])
    elif any(word in user_message for word in ["good", "great", "happy", "well"]):
        bot_message = random.choice(responses["feeling_good"])
    elif any(word in user_message for word in ["sad", "down", "bad", "stressed", "depressed"]):
        bot_message = random.choice(responses["feeling_down"])
    elif any(word in user_message for word in ["angry", "mad", "frustrated", "rage"]):
        bot_message = random.choice(responses["anger"])
    elif any(word in user_message for word in ["dizzy", "lightheaded", "vertigo"]):
        bot_message = random.choice(responses["dizzy"])
    elif any(word in user_message for word in ["anxious", "anxiety", "nervous"]):
        bot_message = random.choice(responses["anxiety"])
    elif any(word in user_message for word in ["tired", "fatigued", "exhausted"]):
        bot_message = random.choice(responses["fatigue"])
    elif any(word in user_message for word in ["confused", "confusion", "uncertain"]):
        bot_message = random.choice(responses["confusion"])
    elif any(word in user_message for word in ["relationship", "partner", "love", "dating"]):
        bot_message = random.choice(responses["relationship"])
    elif "advice" in user_message or "help" in user_message:
        bot_message = random.choice(responses["advice"])
    elif any(word in user_message for word in ["tips", "recommendation"]):
        bot_message = random.choice(responses["tips"])
    elif any(word in user_message for word in ["thank you", "thanks", "thankyou"]):
        bot_message = random.choice(responses["thank_you"])
    elif "ok" in user_message or "okay" in user_message:
        bot_message = random.choice(responses["ok"])
    else:
        bot_message = random.choice(responses["default"])

    return jsonify({"bot_message": bot_message})

if __name__ == "__main__":
    app.run(debug=True)
