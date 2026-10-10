import os

from dotenv import load_dotenv

load_dotenv()

# from langchain.chat_models import ChatOpenAI

# llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


def main() -> None:
    print("Hello from langchain-course!")
    print(os.getenv("OPENAI_API_KEY"))


if __name__ == "__main__":
    main()
