from openai import OpenAI
import openai
import os
from config.settings import Config

print("OpenAI version:", openai.__version__)

# Validate configuration
Config.validate()

# Initialize OpenAI client
client = OpenAI(api_key=Config.OPENAI_API_KEY)

def load_wab_info():
    """Load WAB information from the knowledge base file."""
    if os.path.exists(Config.KNOWLEDGE_BASE_PATH):
        with open(Config.KNOWLEDGE_BASE_PATH, "r", encoding="utf-8") as f:
            return f.read()
    raise FileNotFoundError(f"WAB information file not found: {Config.KNOWLEDGE_BASE_PATH}")

def generate_response(user_input):
    """Generate a response based on WAB information only."""
    wab_info = load_wab_info()

    messages = [
        {"role": "system", "content": (
            "You are a helpful assistant for Western Academy of Beijing (WAB). "
            "You must only answer questions using the content provided below about the school. "
            "Be friendly, informative, and helpful. If the user's question is not relevant to the "
            "WAB information provided, politely redirect them by saying: "
            "'I'm sorry, I can only answer questions about Western Academy of Beijing based on the information I have.'\n\n"
            f"Provided WAB Information:\n{wab_info}"
        )},
        {"role": "user", "content": user_input}
    ]

    try:
        response = client.chat.completions.create(
            model=Config.OPENAI_MODEL,
            messages=messages,
            temperature=Config.OPENAI_TEMPERATURE,
            max_tokens=Config.OPENAI_MAX_TOKENS
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Sorry, I encountered an error: {str(e)}"

def chat():
    """Interactive command-line chat interface (for testing)."""
    wab_info = load_wab_info()

    print("WAB AI Chatbot (type 'exit' to quit)")
    print("Ask me anything about Western Academy of Beijing!")
    print("-" * 50)

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Goodbye! 🐅")
            break
        
        if not user_input:
            continue

        print("WAB AI: ", end="")
        response = generate_response(user_input)
        print(response)

if __name__ == "__main__":
    chat()