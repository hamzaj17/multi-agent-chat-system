import json

class ResearchAgent:
    def __init__(self, kb_path="data/knowledge_base.json"):
        with open(kb_path, "r") as f:
            self.knowledge_base = json.load(f)

    def research(self, query):
        query = query.lower()

        for topic, data in self.knowledge_base.items():
            if topic in query:
                return data["facts"]

        return ["No data found"]
