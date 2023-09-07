import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


def chat_with_ward():
  messages = [{
      "role":
      "system",
      "content":
      "You are a chatbot naned Ward that reluctantly answers questions"
  }]

  while True:
    user_input = input("You: ")

    messages.append({"role": "user", "content": user_input})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.2,
        max_tokens=4000,
    )

    ward_message = completion.choices[0].message["content"]
    print(f"Ward: {ward_message}")

    messages.append({"role": "assistant", "content": ward_message})


if __name__ == "__main__":
  chat_with_ward()
