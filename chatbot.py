
import re


def get_response(user_input):

    if not isinstance(user_input, str) or not user_input.strip():
        return "Please enter a message."

    message = user_input.lower().strip()

    # Greetings
    if re.search(r"\b(hello|hi|hey)\b", message):
        return "Hello! Nice to meet you. How can I help you?"

    # How are you
    elif "how are you" in message:
        return "I'm doing great! How about you?"

    # Name
    elif "your name" in message:
        return "I'm your personal chatbot."

    # Capabilities
    elif "what can you do" in message:
        return "I can chat with you and answer basic questions."

    # Goodbye
    elif re.search(r"\b(bye|goodbye)\b", message):
        return "Goodbye! Have a wonderful day."

    # Default response
    else:
        return "Sorry, I don't understand that yet. Can you ask something else?"
