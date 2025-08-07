from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()

import os
from crewai import LLM

llm = LLM(
    model="openai/gpt-4", # call model by provider/model_name
    temperature=0.5,
    
)
#Create the senior news researcher agent

news_researcher=Agent(
    role='senior researcher',
    goal='Uncover ground breaking technologies in{topic}',
    verbose=True,
    memory=True,
    backstory = (
    "You are a senior researcher skilled at finding the latest tech breakthroughs using web tools like Serper.dev. "
    "You analyze search results quickly and extract only relevant, trusted insights to guide innovation."
),
    llm=llm,
    tools=[tool],
    allow_delegation=True

)

news_writer=Agent(
    role='Writer',
    goal='Narrate compelling tech stories about {topic}',
    verbose=True,
    memory=True,
    backstory=("with a flair for simplifing complex topics,you craft"
               "engaging captatives that captivate and educate, bringing new"
               "discoveries to light in acessible manner"
               ),
    llm=llm,
    tools=[tool],
    allow_delegation=False
)