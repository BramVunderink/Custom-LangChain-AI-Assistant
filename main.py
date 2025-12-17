from dotenv import load_dotenv
import os

load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")

print(gemini_key)

print("Hi I am Albert, how. can i help you today?")

while True:
    user_input = input("You: ")
    if user_input == "exit":
        break
    print(f"Cool, thanks for sharing that {user_input}")
