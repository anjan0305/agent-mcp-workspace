from dotenv import load_dotenv
from langchain.messages import SystemMessage,HumanMessage
from langchain.chat_models import init_chat_model
from langchain_core.tools import tool

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
    
print('The tool name is '+get_weather_reporter.name)
print ('The tool description is '+get_weather_reporter.description)
    