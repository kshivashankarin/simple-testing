from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini"
)

while True:
    user_msg = input("User Message : ")

    if user_msg == "exit":
        print("Exiting form the chat...................")
        break



    response = llm.invoke(user_msg)

    print("AI response : " + response.content)



