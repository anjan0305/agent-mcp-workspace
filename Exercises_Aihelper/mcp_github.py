from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain.messages import HumanMessage
import asyncio
import os


load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_KEY")
qa_prompt=(
    "list me all the files present in my github repository anjan0305/agent-mcp-workspace in the main branch"
    "push my local changes into the main branch"
    "The change is only a new file named mcp_github.py is added with contents inside the Exercises_Aihelper"
)



async def main():
    model=init_chat_model("gpt-4o-mini",model_provider='openai')
    
    client = MultiServerMCPClient(
    {
        "github": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-github"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": GITHUB_TOKEN
      } ,
      "transport":"stdio",
                  }
            }
        )
    tool_list=await client.get_tools()
    agent=create_agent(model,tools=tool_list)
    response=await agent.ainvoke(
        {"messages":[HumanMessage(content=qa_prompt)]}
    )
    print(response["messages"][-1].content)
    


if __name__=="__main__":
    asyncio.run(main())



    
# Your content for mcp_github.py goes here

