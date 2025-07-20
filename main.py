from langchain_openai import ChatOpenAI
from langchain_core.messages.base import BaseMessage
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from typing import Literal, List


class CustomerServiceMessage(HumanMessage):
    type: Literal["customer_service"] = "customer_service"
    pass


class CustomerMessage(HumanMessage):
    type: Literal["customer"] = "customer"
    pass


system_prompt = """
You are a helpful, professional AI assistant designed to assist in customer support conversations between a Customer and a Customer Service Agent.
Your job is to respond only as "Assistant" — answering questions, resolving issues, or helping the Customer Service Agent respond more effectively.
"""

messages: List = [
    SystemMessage(content=system_prompt),
    CustomerMessage(content="Hi, I need help with my order."),
    CustomerServiceMessage(content="Sure, can you provide your order ID"),
    CustomerMessage(content="Yes, it's #12345."),
]


chat = ChatOpenAI(model="gpt-4o-mini", temperature=0)


def main():
    print(chat.invoke(messages))


if __name__ == "__main__":
    main()
