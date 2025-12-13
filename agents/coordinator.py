class Coordinator:
    def __init__(self, research_agent, analysis_agent, memory_agent):
        self.research_agent = research_agent
        self.analysis_agent = analysis_agent
        self.memory_agent = memory_agent

    def handle_query(self, query):
        print("[Coordinator] Received query:", query)

        #try memory only if it is relevant
        memory_result = self.memory_agent.vector_search(query)
        if memory_result:
            print("[Coordinator] Retrieved from memory")
            return memory_result["content"]

        #decide task type
        if "analyze" in query or "compare" in query:
            research_data = self.research_agent.research(query)
            analysis = self.analysis_agent.analyze(research_data)

            self.memory_agent.store(
                topic=query,
                content=analysis,
                source="ResearchAgent",
                agent="AnalysisAgent",
                confidence=0.9
            )
            return analysis

        #simple research query
        research_data = self.research_agent.research(query)
        response = "\n".join(research_data)

        self.memory_agent.store(
            topic=query,
            content=response,
            source="ResearchAgent",
            agent="ResearchAgent",
            confidence=0.8
        )

        return response
