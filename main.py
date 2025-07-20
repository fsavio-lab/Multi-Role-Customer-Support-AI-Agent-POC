from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
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
You assist the based on the customer messages to let the Customer Service respond quickly.
"""

messages: List = [
    SystemMessage(content=system_prompt),
    CustomerMessage(content="Hi, I need help with my order."),
    CustomerServiceMessage(content="Sure, can you provide your order ID"),
    CustomerMessage(content="Yes, it's #12345."),
    CustomerServiceMessage(content="Okay, let me check in my system.")
]


chat = ChatOpenAI(model=os.getenv("OPENAI_MODEL","gpt-4o-mini"), temperature=0)


def main():
    print("AI Agent Response:",chat.invoke(messages).content)


if __name__ == "__main__":
    main()
