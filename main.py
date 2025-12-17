from dotenv import load_dotenv
import os
import gradio as gr

from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")

system_prompt = """
You are Einstein.
Asnwer questions through Eisnteins questioning and reasoning...
You will speak from your point of view. You will share personal things
from your life even when the user don't ask for it. For example,
if the user askss about the  theory of relativity, you will share your personal
experiences with it and not oonly explain the theory.
Answer in 2-6 sentences.
You should have a sense of humor.
"""

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",
                             google_api_key=gemini_key,
                             temperature=0.5
                             )

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    (MessagesPlaceholder(variable_name="history")),
    ("user", "{input}")]
)

chain = prompt | llm | StrOutputParser()

print("Hi I am Albert, how. can i help you today?")

history = []

# while True:
#     user_input = input("You: ")
#     if user_input == "exit":
#         break
#     response = chain.invoke({"input": user_input, "history": history})
#     print(f"Albert: {response}")
#     history.append(HumanMessage(content=user_input))
#     history.append(AIMessage(content=response))

page = gr.Blocks(
    title="Chat with Einstein",
    theme=gr.themes.Soft()
)
with page:
    gr.Markdown(
        """
    # Chat with Einstein
    Welcome to your personal conversation with Albert Einstein
    """)

    chatbot = gr.Chatbot()

    msag = gr.Textbox()

    clear = gr.Button("Clear Chat")

page.launch(share=True)
