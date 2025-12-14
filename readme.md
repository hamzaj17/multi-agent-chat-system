# Multi-Agent Chat System (KRR Assignment)

## Overview

This project implements a **Simple Multi-Agent Chat System** as part of the Knowledge Representation and Reasoning (KRR) assignment. The system shows how multiple agents can work together to answer user queries by sharing tasks, reasoning over stored knowledge, and remembering past interactions.

The system is **console-based**, written in **Python**, and focuses on clarity, collaboration, and explainable behavior rather than complex AI models.

---

## Agents in the System

### 1. Coordinator Agent

* Acts as the manager of the system
* Receives user queries
* Decides which agents are needed based on query complexity
* Sequences agent calls and combines results

### 2. Research Agent

* Retrieves information from a pre-loaded JSON knowledge base
* Simulates web search using structured data
* Returns relevant facts based on query keywords

### 3. Analysis Agent

* Analyzes and summarizes research results
* Performs simple reasoning, comparison, and trade-off analysis

### 4. Memory Agent

* Stores structured memory records
* Each record includes timestamp, topic, content, source, agent, and confidence score
* Uses keyword search and vector similarity to retrieve relevant past knowledge

---

## How the System Works

1. The user enters a query in the console
2. The Coordinator Agent analyzes the query
3. For simple queries, the Research Agent is called
4. For complex queries (analysis or comparison), both Research and Analysis Agents are used
5. The Memory Agent stores the final result
6. For repeated or related queries, memory is reused to avoid redundant work

This flow demonstrates **agent coordination, collaboration, and adaptive decision-making**.

---

## Knowledge Base

* Stored in `data/knowledge_base.json`
* Represents structured domain knowledge
* Used by the Research Agent to retrieve factual information
* Separates knowledge storage from reasoning logic

---

## Memory & Decision-Making

* Memory records are structured (not plain text)
* Vector similarity (TF-IDF) is used for context-aware retrieval
* The Coordinator adapts behavior based on previous interactions
* Graceful fallback is used when data is missing (e.g., "No data found")

---

## Sample Outputs

All required test case outputs are saved in the `outputs/` directory:

* `simple_query.txt`
* `complex_query.txt`
* `memory_test.txt`
* `multi_step.txt`
* `collaborative.txt`

These files demonstrate agent collaboration, reasoning, and memory reuse.

---

## Running the Project Locally

```bash
python main.py
```

Type `exit` to stop the program.

---

## Docker Support

A Dockerfile is included to allow the project to run in a consistent environment.

### Build the Docker Image

```bash
docker build -t multi_agent_chat .
```

### Run the Container

```bash
docker run -it multi_agent_chat
```

Docker ensures the project runs the same way on different machines.

---

## Technologies Used

* Python 3.11
* scikit-learn (for vector similarity)
* Docker

---

## Conclusion

This project demonstrates the core ideas of **Knowledge Representation and Reasoning** through a simple but effective multi-agent system. It highlights agent coordination, structured memory, and adaptive decision-making in a clear and beginner-friendly way.
