import nltk
from nltk.chat.util import Chat, reflections

# Download NLTK package
nltk.download('punkt')

# Chatbot patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! Welcome to Customer Support.", "Hi there! How can I help you today?"]
    ],

    [
        r"what is your name ?",
        ["I am a Customer Service Chatbot."]
    ],

    [
        r"how are you ?",
        ["I'm doing great. Thank you for asking!"]
    ],

    [
        r"what services do you provide ?",
        ["We provide product support, order tracking, and customer assistance."]
    ],

    [
        r"where is my order ?",
        ["Please provide your order ID so we can help track it."]
    ],

    [
        r"how can i contact support ?",
        ["You can contact support at support@example.com"]
    ],

    [
        r"what are your working hours ?",
        ["Our support team is available from 9 AM to 6 PM."]
    ],

    [
        r"bye|exit|quit",
        ["Thank you for chatting with us. Have a nice day!"]
    ],

    [
        r"(.*)",
        ["Sorry, I didn't understand that. Can you please rephrase?"]
    ]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Start chatbot
print("===================================")
print(" Customer Service Chatbot ")
print(" Type 'bye' to exit ")
print("===================================")

chatbot.converse()