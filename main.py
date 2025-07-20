from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from typing import Literal, List
from dotenv import load_dotenv
import os

load_dotenv()


class CustomerServiceMessage(HumanMessage):
    type: Literal["customer_service"] = "customer_service"
    pass


class CustomerMessage(HumanMessage):
    type: Literal["customer"] = "customer"
    pass


system_prompt = """
You are a helpful, professional AI assistant designed to assist in customer support conversations between a Customer and a Customer Service Agent.
Your job is to respond only as "Assistant" — answering questions, resolving issues, or helping the Customer Service Agent respond more effectively.
You should only give recommendation of actions to assist Customer Service to respond quickly based on the customer messages.
"""

messages: List = [
    SystemMessage(content=system_prompt),
    CustomerMessage(content="Hi, I need help with my order."),
    CustomerServiceMessage(content="Sure, can you provide your order ID"),
    CustomerMessage(content="Yes, it's #12345."),
]


chat = ChatOpenAI(model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"), temperature=0)


def main():
    is_ongoing = True
    count = 0
    print(
        "Ask your Query to our customer service agent, Type `end` to conclude the chat"
    )
    print(*[f"{message.type}: {message.content}" for message in messages], sep="\n")
    while is_ongoing and count <= 10:
        customer_query = str(input("Customer Query:"))
        messages.append(CustomerMessage(content=customer_query))
        ai_response = chat.invoke(messages).content
        print("AI Agent Response:", ai_response)
        messages.append(AIMessage(content=ai_response))
        service_query = str(input("Service Query:"))
        messages.append(CustomerServiceMessage(content=service_query))
        if customer_query.__contains__("end"):
            break
        count += 1
    print("Chat have ended.")


if __name__ == "__main__":
    main()
