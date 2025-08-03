def handle_task(message):
    message = message.lower()
    if "hello" in message:
        return "Hi! How can I assist you today?"
    elif "bye" in message:
        return "Goodbye! Have a great day!"
    return None

