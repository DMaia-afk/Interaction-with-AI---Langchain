import os
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory 


template = """ You are an assistant that helps the user better understand how the dollar exchange rate is performing in relation to other popular currencies.
Such as the Brazilian Real, Canadian Dollar, Euro, Rupees, and Yen. Your output should be a simple list with the current dollar ranking and how much it costs for each currency.
1 dollar = X reais

conversation_history:
{history}

user_input:
{input}"""

prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    MessagesPlaceholder(variable_name="history"),
    ("user", "input")
])

llm = ChatGoogleGenerativeAI(model="gemini-1.0-pro", temperature=0.7)

chain = prompt | llm

store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

chain_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history=get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)


def initiate_conversation():
    print("Welcome to the Currency Exchange Rate Assistant!\nType 'exit' to end the conversation.\n")
    while True:
        question = input("You: ")
        if question.lower()=='exit':
            print("Goodbye! Thank you for using the assistant.")
            break
        elif question.strip() == "":
            print("Please enter a valid question.")
            continue

        response = chain_with_history.invoke(
            {"input": question},
            config={'configurable': {"session_id": "default_session"}}
        )
        print(f"Assistant: {response}\n")

if __name__ == "__main__":
    initiate_conversation()
    