import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MemoryAgent:
    def __init__(self):
        self.records = []
        self.vectorizer = TfidfVectorizer()

    def store(self, topic, content, source, agent, confidence):
        self.records.append({
            "timestamp": str(datetime.datetime.now()),
            "topic": topic,
            "content": content,
            "source": source,
            "agent": agent,
            "confidence": confidence
        })

    def vector_search(self, query):
        if len(self.records) < 2:
            return None  # 🔑 avoid premature memory usage

        texts = [r["content"] for r in self.records]
        vectors = self.vectorizer.fit_transform(texts + [query])
        similarities = cosine_similarity(vectors[-1], vectors[:-1])[0]

        best_index = similarities.argmax()

        if similarities[best_index] > 0.4:
            return self.records[best_index]

        return None
