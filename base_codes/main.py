from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
load_dotenv()

model=init_chat_model("gpt-4o-mini",model_provider="openai")
response=model.invoke("Who won Ipl 2025")
print(response.content)

def getWeather(city:str) ->str:
    '''Get Weather for a given city.'''
    return f"Weather is always sunny in {city}"

def sum(a:int,b:int) ->str:
    '''Get product of two numbers'''
    sum=a+b
    return f"The sum is {sum}"


agent=create_agent(
    model="gpt-4o-mini",
    tools=[getWeather,sum],
    system_prompt="You are a helpful assistant",
   

)


result = agent.invoke(
    {"messages": [{"role": "user", "content": "Multiply 8 and 4"}]}
)
print(result["messages"][-1].content_blocks)