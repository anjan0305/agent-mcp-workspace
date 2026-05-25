from dotenv import load_dotenv
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver



load_dotenv()

agent=create_agent(
    model="gpt-4o-mini",
    tools=[],
    system_prompt="You are a helpfull assistant",
    #checkpointer=InMemorySaver()

)

response1=agent.invoke(
{"messages":[{"role":"user","content":"Who is Dhoni?"}]},
{"configurable":{"thread_id":"1"}},
)

response2=agent.invoke(
    {
        "messages":[
            {
                "role":"user",
                "content":"Who is Virat Kohli"
            }
        ]
    },
    {"configurable": {"thread_id":"2"}},
)

response3=agent.invoke(
    {"messages":[
        { "role":"user",
         "content":"When was his debut"
         }
       

    ]
    },
    {"configurable":{"thread_id":"1"}},
)

print(response1["messages"][-1].content)
print('***********')
print(response2["messages"][-1].content)
print('***********')
print(response3["messages"][-1].content)

print(response3)
