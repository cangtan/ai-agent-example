from langchain.chat_models import init_chat_model

messages = [
    {"role": "user", "content": "介绍下你自己"}
]


model = init_chat_model("deepseek-chat",
 model_provider="openai",
  openai_api_key="sk-edeb86a2315f496cabe6fa61ed0b2af6",
   openai_api_base="https://api.deepseek.com/v1")

print(model.invoke(messages).content)