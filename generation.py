from openai import AsyncOpenAI
from run import *

client = AsyncOpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=token_ai,
)

async def generate(text: str):
  completion = await client.chat.completions.create(
    model="deepseek/deepseek-chat-v3.1",
    messages=[
      {
        "role": "user",
        "content": text
      }
    ]
  )
  print(completion)
  return completion.choices[0].message.content