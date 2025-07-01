from openai import OpenAI
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
API_KEY = config['openai']['api_key']
BASE_URL = config['openai']['base_url']
MODEL = config['openai']['model']
messages = [
    {"role": "user", "content": "什么是TPU"}
]

client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)

res = client.chat.completions.create(
    model=MODEL,
    messages=messages
)

print(res.choices[0].message.content)