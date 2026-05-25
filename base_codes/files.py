from langchain.agents import create_agent
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()   

def createFile(fileName:str):
    '''Create a file if doesn't exist with the name as passed by user'''
    try:
        with open(fileName,'x') as f:
            print (f"Create the file {fileName}")
            pass
    except:
          print("File Already exists")
      

def createDirectory(folderName:str):
     '''Create a folder if it doesn't exist'''
     try:
          os.makedirs(folderName,exist_ok=True)
          print(f"Folder created with name {folderName}")
     except:
          print("Folder exists")


agent=create_agent(
    model='gpt-4o-mini',
    tools=[createFile,createDirectory],
    system_prompt='You are a helpful assistant'
)

result=agent.invoke(
    {"messages": [{"role": "user", "content": "Create a folder with name anjan"}]}
)

print(result["messages"][-1].content_blocks)

