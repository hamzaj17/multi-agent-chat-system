from agents.coordinator import Coordinator
from agents.research_agent import ResearchAgent
from agents.analysis_agent import AnalysisAgent
from agents.memory_agent import MemoryAgent

coordinator = Coordinator(
    ResearchAgent(),
    AnalysisAgent(),
    MemoryAgent()
)

print("Type 'exit' to stop\n")

while True:
    query = input("User: ")
    if query.lower() == "exit":
        break

    response = coordinator.handle_query(query)
    print("System:\n", response)
