from langchain_mcp_adapters.client import MultiServerMCPClient
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain.chat_models import init_chat_model
import asyncio




load_dotenv()

async def main():
    model=init_chat_model("gpt-4o-mini",model_provider="openai")
    
    client = MultiServerMCPClient(
    {
        "math": {
            "command": "python",
            # Make sure to update to the full absolute path to your math_server.py file
            "args": ["/path/to/math_server.py"],
            "transport": "stdio",
        }
    }
   )
    mcp_tools = await client.get_tools()
    agent = create_agent(model, tools=mcp_tools)
    response = await agent.ainvoke(
        {
            "messages": [
                HumanMessage(content="What is 453 plus 872? Use your math tool.")
            ]
        }
    )


    print(response["messages"][-1].content)


# Run the asynchronous main execution loop
if __name__ == "__main__":
    asyncio.run(main())



