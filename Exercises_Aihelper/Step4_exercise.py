from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain.chat_models import init_chat_model
from langchain.messages import SystemMessage,HumanMessage



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
    

model=init_chat_model("gpt-4o-mini",model_provider='openai')
toolsList=[get_weather_reporter]
agent=create_agent(model,
                   toolsList)


response=agent.invoke({
    "messages":[HumanMessage(content="Tell me the weather of london")]
})
print(response["messages"][-1].content)