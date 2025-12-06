from src.agents.llm_client import LLMClient

class ResearcherAgent:
    def __init__(self):
        self.llm = LLMClient()

    def run(self, topic: str) -> str:
        prompt = (
            f"Generate deeply researched information about: {topic}.\n"
            "Include key insights and factual knowledge."
        )
        return self.llm.chat(prompt)
