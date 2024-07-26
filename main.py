import os
from crewai import Crew


from textwrap import dedent

from agents import TravelAgents
from agent_tasks import TravelTasks

class TripCrew:
    def __init__(self, origin, cities, duration, date_range, interests):
        self.origin = origin
        self.cities = cities
        self.duration = duration
        self.date_range = date_range
        self.interests = interests
    
    def plan_trip(self):
        # define your custom agents and tasks
        agents = TravelAgents()
        tasks = TravelTasks()
        
        # define your custom agents 
        expert_travel_agent = agents.expert_travel_agent()
        city_selection_expert = agents.city_selection_expert()
        local_tour_guide = agents.local_tour_guide()
        
        #custom tasks and include agents name
        plan_itinerary = tasks.plan_itinerary(
            expert_travel_agent,
            self.cities,
            self.date_range,
            self.duration,
            self.interests
        )
        
        identify_cities = tasks.identify_city(
            city_selection_expert,
            self.cities,
            self.date_range,
            self.interests,
            self.origin
        )
        
        gather_city_info = tasks.gather_city_info(
            local_tour_guide,
            self.cities,
            self.date_range,
            self.interests
        )
        
        # Define custom crew
        crew = Crew(
            agents=[expert_travel_agent, city_selection_expert, local_tour_guide],
            tasks= [plan_itinerary, identify_cities, gather_city_info],
            verbose=True
        )
        
        result = crew.kickoff()
        return result
    

if __name__ == "__main__":
    print("## Welcome to Trip Planner Crew")
    print('-------------------------------')
    origin = input(
        dedent("""
      From where will you be traveling from?
    """))
    cities = input(
        dedent("""
      What are the cities options you are interested in visiting?
    """))
    duration = input(
        dedent("""
      How many days are you planning to travel?
    """))
    date_range = input(
        dedent("""
      What is the date range you are interested in traveling?
    """))
    interests = input(
        dedent("""
      What are some of your high level interests and hobbies?
    """))
    
    trip_crew = TripCrew(origin, cities, duration, date_range, interests)
    result = trip_crew.plan_trip()
    
    print("## Trip Planning Completed")
    print('-------------------------------')
    print("-----Here is you Trip Plan-----")
    print(result)