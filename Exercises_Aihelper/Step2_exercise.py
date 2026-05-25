from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage,HumanMessage
load_dotenv()


model=init_chat_model("gpt-4o-mini",model_provider="openai")
chat_history=[
    SystemMessage(content="You are a chef. Give extremely short, one-sentence recipe answers."),
    HumanMessage(content="How do I make an omelet?")
]
response=model.invoke(chat_history)
print(response.content)
#print(response["messages"][-1].content_blocks)
#print(result["messages"][-1].content_blocks)



