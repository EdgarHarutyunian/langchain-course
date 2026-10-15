from dotenv import load_dotenv
import os
load_dotenv()


def main():
    print("Hello from langchain-course!")
    print("OpenAI API Key:", os.getenv("OPENAI-API-KEY"))



if __name__ == "__main__":
    main()
