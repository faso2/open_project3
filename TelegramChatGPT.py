import telegram
import asyncio
from openai import OpenAI

client = OpenAI(
    api_key="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"
  )

completion = client.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  messages=[
    {"role": "system", "content": "너는 이제 훌륭한 야구평론가야"},
    {"role": "user", "content": "뉴욕 메츠에 대한 너의 생각을 하나 써줘. json"}
  ],
  response_format={"type": "json_object"}
)

token = "6879534572:AAF8OWh2TNFfW3CyxvLVvfigaknSY5HXtJ8"
bot = telegram.Bot(token=token)
chat_id = "@gometsbot"
text = completion.choices[0].message.content
print(text)
asyncio.run(bot.sendMessage(chat_id=chat_id, text=text))

print(completion.choices[0].message.content)