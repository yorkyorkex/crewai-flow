from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


@CrewBase
class DestinationResearchCrew:
    """Destination Research Crew for comprehensive travel destination analysis"""

    agents: List[BaseAgent]
    tasks: List[Task]

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def destination_researcher(self) -> Agent:
        """Primary destination research specialist"""
        return Agent(
            config=self.agents_config["destination_researcher"],  # type: ignore[index]
        )

    @agent
    def travel_cost_analyst(self) -> Agent:
        """Travel budget and cost analysis expert"""
        return Agent(
            config=self.agents_config["travel_cost_analyst"],  # type: ignore[index]
        )

    @agent
    def cultural_advisor(self) -> Agent:
        """Cultural and local customs expert"""
        return Agent(
            config=self.agents_config["cultural_advisor"],  # type: ignore[index]
        )

    @task
    def research_destination_overview(self) -> Task:
        """Research comprehensive destination information"""
        return Task(
            config=self.tasks_config["research_destination_overview"],  # type: ignore[index]
        )

    @task
    def analyze_travel_costs(self) -> Task:
        """Analyze and estimate travel costs"""
        return Task(
            config=self.tasks_config["analyze_travel_costs"],  # type: ignore[index]
        )

    @task  
    def provide_cultural_insights(self) -> Task:
        """Provide cultural insights and practical advice"""
        return Task(
            config=self.tasks_config["provide_cultural_insights"],  # type: ignore[index]
        )

    @task
    def compile_destination_research(self) -> Task:
        """Compile all research into comprehensive report"""
        return Task(
            config=self.tasks_config["compile_destination_research"],  # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Destination Research Crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )