from openai import OpenAI
from hendlers import token_ai

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=token_ai,
)

completion = client.chat.completions.create(
  model="deepseek/deepseek-chat-v3.1",
  messages=[
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]
)
print(completion.choices[0].message.content)