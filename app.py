from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_response(user_input):
    user_input = user_input.lower()

    # Enhanced rule-based responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a program, but I'm here to help you!"
    elif "stress" in user_input:
        return "It's normal to feel stressed. Take deep breaths and try to relax."
    elif "help" in user_input:
        return "I’m here to help! What’s on your mind?"
    elif "study" in user_input:
        return "Studying can be tough! Make sure to take breaks and stay organized."
    elif "exam" in user_input:
        return "Exams can be stressful. Try to manage your time wisely and review consistently."
    elif "mental health" in user_input:
        return "Your mental health is important. It's okay to seek help when you need it."
    elif "bored" in user_input:
        return "Feeling bored? Maybe try a new hobby or go for a walk to clear your mind!"
    elif "anxiety" in user_input:
        return "It's okay to feel anxious. Consider talking to someone you trust or practicing mindfulness."
    elif "motivation" in user_input:
        return "Sometimes we all need a little motivation! Remember your goals and take one step at a time."
    elif "friends" in user_input:
        return "Friends are important! Make sure to connect with them and share your thoughts."
    elif "career" in user_input:
        return "Thinking about your career? It's great to plan ahead! Consider exploring different fields."
    elif "thank you" in user_input:
        return "You're welcome! I'm here to help whenever you need."
    elif "exit" in user_input:
        return "Thank you for chatting! Take care."
    else:
        return "I'm sorry, I don't understand. Can you rephrase that?"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-response', methods=['POST'])
def respond():
    user_message = request.json['message']
    bot_response = get_response(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
