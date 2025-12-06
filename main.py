from src.agents.researcher_agent import ResearcherAgent
from src.agents.writer_agent import WriterAgent

if __name__ == "__main__":
    topic = input("Enter research topic: ")

    researcher = ResearcherAgent()
    writer = WriterAgent()

    research_output = researcher.run(topic)
    final_report = writer.run(research_output)

    print("\n=== REPORT ===\n")
    print(final_report)
