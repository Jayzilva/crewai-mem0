# CrewAI + Mem0 Integration for Personalized Travel Recommendations

This project demonstrates how to use CrewAI with Mem0 for creating personalized travel recommendations. The system uses a memory-driven approach to provide travel suggestions tailored to a user's preferences. The main goal is to give users travel recommendations based on their preferences for cultural experiences, local cuisine, and mid-range accommodations, all while avoiding tourist traps.

## Prerequisites

Before running the project, ensure you have the following:

- Python 3.7+ installed
- API keys for the services used in this project:
  - [Mem0 API Key](https://mem0.com) (for storing and retrieving user preferences)
  - [OpenAI API Key](https://beta.openai.com/signup/) (for AI-related tasks)
  - [Serper API Key](https://serper.dev/) (for real-time search capabilities)

### Install the required dependencies:

```bash
pip install crewai mem0 crewai-tools openai
```

How It Works
Step 1: Initialize User Memory
The first step is to initialize the user's preferences in Mem0. This stores the user's travel preferences such as preferred activities, budget, and specific likes/dislikes regarding travel.

Step 2: Create a Travel Recommendation Agent
An agent is created to handle travel recommendations based on the stored preferences. The agent uses Mem0 for remembering user preferences and adjusts recommendations accordingly.

Step 3: Create a Task for the Agent
A task is created to recommend personalized travel destinations, experiences, and accommodations for a given location. The agent uses user preferences to tailor suggestions, avoiding popular tourist spots and focusing on cultural experiences and local cuisine.

Step 4: Set Up a Crew with Mem0 Integration
The CrewAI system is used to manage the agents and tasks. The crew integrates Mem0 for memory storage and retrieval, ensuring the agent remembers user preferences and produces relevant, personalized recommendations.

Step 5: Run the Process
The process is run with the run_poc function, which will initialize the user memory (only needed once), create an agent, generate a task, and execute the recommendation process.

Usage
To use this project, run the following script:

bash
Copy code
python main.py
This will:

Initialize the user memory in Mem0.
Create a travel recommendation agent.
Create a task for a given destination.
Setup CrewAI with memory.
Output personalized travel recommendations.
Example Usage
python
Copy code
# Example destination for personalized recommendations
destination = "Kyoto, Japan"
run_poc(destination)
Project Structure
plaintext
Copy code
├── main.py                    # Main script to run the POC
├── requirements.txt           # List of project dependencies
├── .env                       # Configuration file for API keys (not included in version control)
├── README.md                  # Project README
└── README_Generated.md         # Automatically generated recommendations output
Key Concepts
Mem0
Mem0 is a memory management system that allows you to store and retrieve user data over time, making it ideal for use cases like personal assistants, recommendation systems, and other AI-driven applications that need to remember user preferences.

In this project, Mem0 is used to store user travel preferences and retrieve them whenever the agent generates travel recommendations.

CrewAI
CrewAI is a powerful tool that enables you to orchestrate complex agent tasks using multiple agents and external tools, ensuring that each agent can focus on specific parts of a task. CrewAI enables you to create processes that are memory-driven and modular.

In this project, CrewAI is used to manage agents, tasks, and memory integration, which allows for the efficient management of personalized recommendations and other user interactions.