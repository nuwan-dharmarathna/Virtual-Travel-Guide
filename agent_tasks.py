from crewai import Task
from textwrap import dedent

# this is an example of how to define custom tasks.
# you can define as many tasks as you want.
# you can also define custom agents in agents.py

"""
    Creating Tasks Cheat Sheet:
    - Begin with the end in mind. Identify the specific outcome your tasks are aiming to achieve.
    - Break down the outcome into actionable tasks, assigning each task to the appropriate agent.
    - Ensure tasks are descriptive, providing clear instructions and expected deliverables.

    Goal:
    - Develop a detailed itinerary, including city selection, attractions, and practical travel advice.

    Key Steps for Task Creation:
    1. Identify the Desired Outcome: Define what success looks like for your project.
        - A detailed 7 day travel itenerary.

    2. Task Breakdown: Divide the goal into smaller, manageable tasks that agents can execute.
        - Itenerary Planning: develop a detailed plan for each day of the trip.
        - City Selection: Analayze and pick the best cities to visit.
        - Local Tour Guide: Find a local expert to provide insights and recommendations.

    3. Assign Tasks to Agents: Match tasks with agents based on their roles and expertise.

    4. Task Description Template:
    - Use this template as a guide to define each task in your CrewAI application. 
    - This template helps ensure that each task is clearly defined, actionable, and aligned with the specific goals of your project.

    Template:
    ---------
    def [task_name](self, agent, [parameters]):
        return Task(description=dedent(f'''
        **Task**: [Provide a concise name or summary of the task.]
        **Description**: [Detailed description of what the agent is expected to do, including actionable steps and expected outcomes. 
        This should be clear and direct, outlining the specific actions required to complete the task.]

        **Parameters**: 
        - [Parameter 1]: [Description]
        - [Parameter 2]: [Description]
        ... [Add more parameters as needed.]

        **Note**: [Optional section for incentives or encouragement for high-quality work. This can include tips, additional context, or motivations to encourage agents to deliver their best work.]

        '''), agent=agent)

"""

class TravelTasks:
    
    def plan_itinerary(self, agent, city, travel_dates, duration, interests):
        return Task(
            description = dedent(
                f"""
                    **Task**: Developing a Detailed Travel Itinerary for {duration} Days
                    
                    **Description**: Analyze and select the best city for the trip based on specific 
                                    criteria such as weather patterns, seasonal events, and travel costs. 
                                    This task involves comparing multiple cities, considering factors like current weather 
                                    conditions, upcoming cultural or seasonal events, and overall travel expenses. 
                                    Your final answer must be a detailed report on the chosen city, 
                                    including actual flight costs, weather forecast, and attractions.
                                    
                    **Parameters**: 
                    - City: {city}
                    - Trip Date: {travel_dates}
                    - Duration: {duration} days
                    - Traveler Interests: {interests}    
                """
            ),
            agent=agent,
            expected_output=dedent(
                f"""
                    A detailed itinerary for {city}, including flight costs, weather forecast, and attractions.
                """
            ),
        )
        
    def identify_city(self, agent, city, travel_dates, interests, origin, duration):
        return Task(
            description = dedent(
                f"""
                    **Task**: Gathering Information on the Selected City
                    **Description**: Compile an in-depth guide for the selected city, gathering information about 
                        key attractions, local customs, special events, and daily activity recommendations. 
                        This guide should provide a thorough overview of what the city has to offer, including 
                        hidden gems, cultural hotspots, must-visit landmarks, weather forecasts, and high-level costs.

                    **Parameters**: 
                    - Origin: {origin}
                    - Cites: {city}
                    - Trip Date: {travel_dates}
                    - Duration: {duration} days
                    - Traveler Interests: {interests}      
                """
            ),
            agent=agent,
            expected_output=dedent(
                f"""
                    An in-depth guide for {city} with attractions, local customs, events, and recommendations.
                """
            ),
        )
        
    def gather_city_info(self, agent, city, travel_dates, interests, duration):
        return Task(
            description = dedent(
                f"""
                    **Task**: Identifying the Best Cities to Visit
                    **Description**: Compile an in-depth guide for the selected city, gathering information about 
                        key attractions, local customs, special events, and daily activity recommendations. 
                        This guide should provide a thorough overview of what the city has to offer, including 
                        hidden gems, cultural hotspots, must-visit landmarks, weather forecasts, and high-level costs.

                    **Parameters**: 
                    - Cites: {city}
                    - Trip Date: {travel_dates}
                    - Duration: {duration} days
                    - Traveler Interests: {interests}
                """
            ),
            agent=agent,
            expected_output=dedent(
                f"""
                    Information about {city} including key attractions, customs, events, and recommendations.
                """
            ),
        )