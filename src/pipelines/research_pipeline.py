from src.agents.researcher_agent import ResearcherAgent
from src.agents.analyzer_agent import AnalyzerAgent
from src.agents.writer_agent import WriterAgent
from src.utils.logger import logger

class ResearchPipeline:
    def __init__(self, allow_network: bool = True):
        self.researcher = ResearcherAgent(allow_network=allow_network)
        self.analyzer = AnalyzerAgent()
        self.writer = WriterAgent()

    def run(self, query: str) -> str:
        raw_docs = self.researcher.run(query)
        analyzed = self.analyzer.run(raw_docs)
        report = self.writer.run(analyzed)
        return report
