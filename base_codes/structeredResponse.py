from dotenv import load_dotenv
from langchain.agents import create_agent
from pydantic import BaseModel

load_dotenv()

class mailResponse(BaseModel):
    Century1:str
    Year1:str
    Opposition1:str
    Ground1:str
    Century2:str
    Year2:str
    Opposition2:str
    Ground2:str
    Century3:str
    Year3:str
    Opposition3:str
    Ground3:str


agent=create_agent(
    model="gpt-4o-mini",
    tools=[],
    system_prompt="You are a helpful assistant",
    response_format=mailResponse
)

response=agent.invoke(
{"messages":[{"role":"user","content":"List the last 3 century details of sourav ganguly"}]}
)


print(response["structured_response"])
#print(response["messages"][1].content)