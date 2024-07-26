from crewai import Agent
from textwrap import dedent

from langchain_openai import ChatOpenAI

import os
from dotenv import load_dotenv

load_dotenv()

# thiss is an example of how to define custom agents
# you can define as many agents as you want
# you can also define custom tasks in tasks.py

"""
    Creating Agents Cheat Sheet:
    - Think like a boss. Work backwards from the goal and think which employee  you need to hire to get the job done.
    - Define the Captain of the crew who orient the other agents towards the goal. 
    - Define which experts the captain needs to communicate with and delegate tasks to.
        Build a top down structure of the crew.

    Goal:
    - Create a 7-day travel itinerary with detailed per-day plans,
        including budget, packing suggestions, and safety tips.

    Captain/Manager/Boss:
    - Expert Travel Agent

    Employees/Experts to hire:
    - City Selection Expert 
    - Local Tour Guide


    Notes:
    - Agents should be results driven and have a clear goal in mind
    - Role is their job title
    - Goals should actionable
    - Backstory should be their resume
"""

class TravelAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0.5,
            api_key=os.getenv("OPENAI_API_KEY")
        )
    
    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(f"""
                             Expert in travel planing anf logistics.
                             I have decades of expereince making travel iteneraries."""),
            goal=dedent(f"""
                        Create a travel itinerary for the given number of days with detailed per-day plans, 
                        including budget, packing suggestions, and safety tips."""),
            # tools=[tool1, tool2],
            verbose=True,
            llm = self.OpenAIGPT35,
        )
    
    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(f"""
                             Expert at analyzing travel data to pick ideal destinations."""),
            goal=dedent(f"""
                        Select the best cities based on weather, season, prices, and traveler interests"""),
            # tools=[tool1, tool2],
            verbose=True,
            llm = self.OpenAIGPT35,
        )
        
    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(f"""
                             Knowledgeable local guide with extensive information about the city, it's attractions and customs"""),
            goal=dedent(f"""
                        Provide the BEST insights about the selected city"""),
            # tools=[tool1, tool2],
            verbose=True,
            llm = self.OpenAIGPT35,
        )