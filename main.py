import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


def chat_with_ward():
  messages = [{
      "role":
      "system",
      "content":
      "Your name is Sydney. You are a young woman who hangs out on the dark web on channels like 4Chan and Reddit. This of course reflects the way you respond to the user in a typical 4Chan / Reddit style."
  }]

  while True:
    user_input = input("You: ")

    messages.append({"role": "user", "content": user_input})

    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.2,
        max_tokens=4000,
    )

    ward_message = completion.choices[0].message["content"]
    print(f"Ward: {ward_message}")

    messages.append({"role": "assistant", "content": ward_message})


if __name__ == "__main__":
  chat_with_ward()
