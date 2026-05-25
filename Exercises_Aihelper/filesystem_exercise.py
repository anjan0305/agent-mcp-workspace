from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain.chat_models import init_chat_model
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient


load_dotenv()

async def main():
    model=init_chat_model("gpt-4o-mini",model_provider="openai")

    client = MultiServerMCPClient(
    {
        "filesystem": {
            "command": "npx",
            "args": [
                    "-y",
                    "@modelcontextprotocol/server-filesystem",
                    "C:/Users/anjan/OneDrive/Desktop/AI Details/Agentic_AI_Classes/Agents_class1"
                     ],
            "transport":"stdio",
            }
        }
    )

    mcp_tools=await client.get_tools()
    agent=create_agent(model,tools=mcp_tools)
    response= await agent.ainvoke(
        {"messages":[HumanMessage("Create a File with name Anjan")]}
    )
    print(response["messages"][-1].content)


if __name__=="__main__":
    asyncio.run(main())
