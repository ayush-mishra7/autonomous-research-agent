from src.agents.llm_client import LLMClient

class WriterAgent:
    def __init__(self):
        self.llm = LLMClient()

    def run(self, research_text: str) -> str:
        prompt = (
            "Convert the following research text into a structured formal report:\n\n"
            "FORMAT:\n"
            "1. Executive Summary\n"
            "2. Key Insights\n"
            "3. Evidence\n"
            "4. Limitations\n\n"
            f"Research Text:\n{research_text}"
        )
        return self.llm.chat(prompt)
