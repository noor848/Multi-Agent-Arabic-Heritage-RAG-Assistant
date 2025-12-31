from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.tools import BaseTool
from typing import List, Type
from pydantic import BaseModel, Field
from .tools.heritage_tool import HeritageTool
from .tools.language_detection import LanguageDetectionTool
from .tools.weather_tool import WeatherTool
from transformers import pipeline


txt_tool = HeritageTool()
language_tool = LanguageDetectionTool()
weather_tool = WeatherTool()


@CrewBase
class RagCrewai():
    """Multi-agent crew with delegation"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # ======================
    # AGENTS
    # ======================
    @agent
    def manager(self) -> Agent:
        """Manager agent that orchestrates and delegates"""
        return Agent(
            config=self.agents_config['manager'],
            llm=LLM(
                model="ollama/aya-expanse:8b",
                base_url="http://localhost:11434",
            ),
            allow_delegation=True,
            verbose=True,
        )

    @agent
    def language_detector(self) -> Agent:
        """Detects if question is in Arabic or English"""
        return Agent(
            config=self.agents_config['language_detector'],
            llm=LLM(
                model="ollama/aya-expanse:8b",
                base_url="http://localhost:11434",
            ),
            tools=[language_tool],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def heritage_expert(self) -> Agent:
        """Searches heritage and historical information"""
        return Agent(
            config=self.agents_config['heritage_expert'],
            llm=LLM(
                model="ollama/aya-expanse:8b",
                base_url="http://localhost:11434",
            ),
            tools=[txt_tool],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def weather_specialist(self) -> Agent:
        """Provides weather forecasts"""
        return Agent(
            config=self.agents_config['weather_specialist'],
            llm=LLM(
                model="ollama/aya-expanse:8b",
                base_url="http://localhost:11434",
            ),
            tools=[weather_tool],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def reporter(self) -> Agent:
        """Formats final response in correct language"""
        return Agent(
            config=self.agents_config['reporter'],
            llm=LLM(
                model="ollama/aya-expanse:8b",
                base_url="http://localhost:11434",
            ),
            allow_delegation=False,
            verbose=True,
        )

    # ======================
    # TASKS
    # ======================

    @task
    def detect_language_task(self) -> Task:
        return Task(
            config=self.tasks_config['detect_language_task'],
            agent=self.language_detector()
        )

    @task
    def heritage_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['heritage_research_task'],
            agent=self.heritage_expert()
        )

    @task
    def weather_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['weather_research_task'],
            agent=self.weather_specialist()
        )

    @task
    def format_report_task(self) -> Task:
        return Task(
            config=self.tasks_config['format_report_task'],
            agent=self.reporter()
        )

    # ======================
    # CREW
    # ======================
    @crew
    def crew(self) -> Crew:
        """Creates the crew with hierarchical process"""
        return Crew(
            agents=[
                self.language_detector(),
                self.heritage_expert(),
                self.weather_specialist(),
                self.reporter()
            ],
            tasks=[
                self.detect_language_task(),
                self.heritage_research_task(),
                self.weather_research_task(),
                self.format_report_task()
            ],
            process=Process.hierarchical,
            manager_agent=self.manager(),
            verbose=True,
        )