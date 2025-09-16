from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


@CrewBase
class ItineraryPlanningCrew:
    """Itinerary Planning Crew for creating detailed travel itineraries"""

    agents: List[BaseAgent]
    tasks: List[Task]

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def itinerary_planner(self) -> Agent:
        """Master travel itinerary planner"""
        return Agent(
            config=self.agents_config["itinerary_planner"],  # type: ignore[index]
        )

    @agent
    def activity_specialist(self) -> Agent:
        """Travel activities and experiences curator"""
        return Agent(
            config=self.agents_config["activity_specialist"],  # type: ignore[index]
        )

    @agent
    def logistics_coordinator(self) -> Agent:
        """Travel logistics and transportation expert"""
        return Agent(
            config=self.agents_config["logistics_coordinator"],  # type: ignore[index]
        )

    @task
    def plan_daily_structure(self) -> Task:
        """Plan the overall daily structure for the trip"""
        return Task(
            config=self.tasks_config["plan_daily_structure"],  # type: ignore[index]
        )

    @task
    def curate_activities(self) -> Task:
        """Curate specific activities and experiences for each day"""
        return Task(
            config=self.tasks_config["curate_activities"],  # type: ignore[index]
        )

    @task  
    def optimize_logistics(self) -> Task:
        """Optimize logistics and timing for each day"""
        return Task(
            config=self.tasks_config["optimize_logistics"],  # type: ignore[index]
        )

    @task
    def compile_itinerary(self) -> Task:
        """Compile everything into a comprehensive itinerary"""
        return Task(
            config=self.tasks_config["compile_itinerary"],  # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Itinerary Planning Crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )