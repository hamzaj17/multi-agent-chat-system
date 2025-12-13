class AnalysisAgent:
    def analyze(self, items):
        result = "Analysis Summary:\n"
        for item in items:
            result += f"- {item}\n"

        result += "\nKey Trade-offs:\n"
        result += "- Performance vs computational cost\n"
        result += "- Accuracy vs efficiency\n"

        return result
