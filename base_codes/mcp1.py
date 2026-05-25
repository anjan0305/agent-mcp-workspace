from langchain_mcp_adapters.client import MultiServerMCPClient
from dotenv import load_dotenv
from langchain.agents import create_agent
import asyncio
import os

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_KEY")

async def run_agent():
    client = MultiServerMCPClient(
        {
        "filesystem": {
                "command": "npx",
                "args": [
                    "-y",
                    "@modelcontextprotocol/server-filesystem",
                    "C:/Users/anjan/OneDrive/Desktop/AI Details/Agentic_AI_Classes/Agents_class1",
      ],
    
            "transport": "stdio",
        },

         "github": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-github"
      ],    
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": GITHUB_TOKEN
      },
      "transport": "stdio", 
    },

       

        }
    )
    tools = await client.get_tools()
    agent = create_agent("openai:gpt-4o-mini", tools)
    response=await agent.ainvoke(
        {"messages":"create a file names requirements.txt in my github repository anjan0305/GenerativeAi and place a binary search code in c++"}
    )


    print(response["messages"][-1].content)


if __name__ == "__main__":
  asyncio.run(run_agent())


