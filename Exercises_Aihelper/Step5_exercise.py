from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
from langchain.messages import HumanMessage

load_dotenv()

@tool
def get_weather_reporter (city_name:str):
    '''This function derives the weather of the city'''
    if city_name=="Delhi":
        return "It is hot and 40°C"
    elif city_name=="London":
        return "It is rainy and 15°C"
    else:
        return "Weather data not available for this city."
    

model=init_chat_model("gpt-4o-mini",model_provider="openai")

tools_list=[get_weather_reporter]
memory_bank=InMemorySaver()

agent=create_agent(model,
                  tools=tools_list,
                   checkpointer=memory_bank )




response1=agent.invoke(
    {"messages":[HumanMessage("Hi, this is Anjan tell me the weather of London")]},
    {"configurable":{"thread_id":"session1"}}
)

response2=agent.invoke(
    {"messages":[HumanMessage("Hi this is Virat Kohli")]},
    {"configurable":{"thread_id":"session2"}}
)

response3=agent.invoke(
    {"messages":[HumanMessage("Who am i ?")]},
    {"configurable":{"thread_id":"session1"}}
)


print(response1["messages"][-1].content)
print(response2["messages"][-1].content)
print(response3["messages"][-1].content)


