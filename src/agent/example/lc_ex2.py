from langchain.chat_models import init_chat_model

import configparser
config = configparser.ConfigParser()
config.read('config.ini')
API_KEY = config['openai']['api_key']
BASE_URL = config['openai']['base_url']
MODEL = config['openai']['model']

messages = [
    {"role": "user", "content": "介绍下你自己"}
]


model = init_chat_model(MODEL,
 model_provider="openai",
  openai_api_key=API_KEY,
   openai_api_base=BASE_URL)

print(model.invoke(messages).content)