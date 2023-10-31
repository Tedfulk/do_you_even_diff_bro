# import openai
# from models import GPTRequest
from llm import prompt


def main():
    test_prompt = "ping"
    response = prompt(test_prompt)
    print(response)


main()
