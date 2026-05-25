from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain.messages import HumanMessage
import asyncio



load_dotenv()

qa_prompt = (
"Go to the website 'https://www.wikipedia.org/'. "
    "Locate the search input box, type 'Software engineering' into it, and press Enter to search. "
    "Once the page loads, tell me the exact URL of the page you landed on."
)

async def main():
    model=init_chat_model("gpt-4o-mini",model_provider="openai")
    client=MultiServerMCPClient(
        {
            "playwright": {
            "command": "npx",
            "args": [
                "@playwright/mcp@latest"
                    ],
                "transport":'stdio',
                }
            }
        )
    print("Connecting to Playwright MCP Server...")
    mcp_tools = await client.get_tools()
    print(f"Connected successfully! Discovered {len(mcp_tools)} tools.")
  
    agent=create_agent(model,tools=mcp_tools)
    print("Launching autonomous browser workflow...")
    response=await agent.ainvoke(
        {"messages":[HumanMessage(content=qa_prompt)]}
    )
    print("\n--- Final QE Execution Report ---")
    print(response["messages"][-1].content)

    
if __name__=="__main__":
    asyncio.run(main())
