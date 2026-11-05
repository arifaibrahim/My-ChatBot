def get_response(user_input):

    message = user_input.lower()

    if "hello" in message or "hi" in message:
        return "Hello! Nice to meet you."

    elif "how are you" in message:
        return "I'm doing great! How about you?"

    elif "your name" in message:
        return "I'm your personal chatbot."

    elif "what can you do" in message:
        return "I can chat with you and answer basic questions."

    elif "bye" in message:
        return "Goodbye! Have a wonderful day."

    else:
        return "Sorry, I don't understand that yet."

