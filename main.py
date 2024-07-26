from crewai import Crew

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
            self.origin,
            self.duration
            
        )
        
        gather_city_info = tasks.gather_city_info(
            local_tour_guide,
            self.cities,
            self.date_range,
            self.interests,
            self.duration,
        )
        
        # Define custom crew
        crew = Crew(
            agents=[expert_travel_agent, city_selection_expert, local_tour_guide],
            tasks= [plan_itinerary, identify_cities, gather_city_info],
            verbose=True
        )
        
        result = crew.kickoff()
        return result
    
