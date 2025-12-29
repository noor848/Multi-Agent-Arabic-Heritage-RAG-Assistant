from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from .tools.arabic_heritage_tool import ArabicHeritageTool

txt_tool = ArabicHeritageTool()

@CrewBase
class RagCrewai():
    """RagCrewai crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def guidance(self) -> Agent:
        return Agent(
            config=self.agents_config['guidance'], # type: ignore[index]
            llm=LLM(
                model="ollama/aya-expanse:8b",
                base_url="http://localhost:11434"
            ),
            tools=[txt_tool],
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['guidance_task'], # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the RagCrewai crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
