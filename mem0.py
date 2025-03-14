import os
from mem0 import MemoryClient
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

# Configuration
os.environ["MEM0_API_KEY"] = ""
os.environ["OPENAI_API_KEY"] = ""
os.environ["SERPER_API_KEY"] = ""

# Initialize Mem0 client
mem0_client = MemoryClient()

# Define a unique user ID for our POC
USER_ID = "poc_user_1"

# Step 1: Store some initial user preferences to establish memory
def initialize_user_memory():
    """Store initial user preferences in Mem0"""
    print("Initializing user memory in Mem0...")

    # Simple conversation with preferences
    initial_conversation = [
        {"role": "user", "content": "I'm looking for travel recommendations."},
        {"role": "assistant", "content": "What kind of activities do you enjoy when traveling?"},
        {"role": "user", "content": "I enjoy cultural experiences and local cuisine. I prefer to avoid touristy spots."},
        {"role": "assistant", "content": "Do you have any budget constraints?"},
        {"role": "user", "content": "I prefer mid-range accommodations and experiences."}
    ]

    # Store in Mem0
    mem0_client.add(initial_conversation, user_id=USER_ID)
    print("User memory initialized successfully!")

    # Verify memory was stored properly
    try:
        test_result = mem0_client.search("travel preferences", user_id=USER_ID)
        print(f"Memory verification successful! Found: {len(test_result)} related memories")
    except Exception as e:
        print(f"Memory verification failed: {str(e)}")

# Step 2: Create an agent with Mem0 memory capabilities
def create_recommendation_agent():
    """Create a recommendation agent that uses memory"""
    print("Creating recommendation agent...")

    # Optional: Add search tool for real data
    search_tool = SerperDevTool()

    return Agent(
        role="Travel Recommendation Specialist",
        goal="Provide personalized travel recommendations based on user preferences",
        backstory="""You are an expert travel consultant who specializes in creating
        personalized recommendations. You're known for remembering user preferences
        and tailoring suggestions to individual tastes.""",
        verbose=True,
        allow_delegation=False,
        memory=True,  # Enable agent memory
        tools=[search_tool]
    )

# Step 3: Define a task for the agent
def create_recommendation_task(agent, destination):
    """Create a task to recommend places based on user preferences"""
    print(f"Creating recommendation task for {destination}...")

    return Task(
        description=f"""
        Based on the user's stored preferences, recommend places to visit,
        eat and stay in {destination}. Focus on cultural experiences and
        local cuisine, avoiding tourist traps. Target mid-range budget options.

        Remember to reference any relevant information from their past conversations.
        """,
        expected_output=f"A personalized list of recommendations for {destination} tailored to the user's preferences",
        agent=agent
    )

# Step 4: Set up a crew with Mem0 integration
def setup_memory_crew(agent, task):
    """Configure a crew with Mem0 memory integration"""
    print("Setting up crew with Mem0 memory integration...")

    # Create a crew with properly configured memory
    return Crew(
        agents=[agent],
        tasks=[task],
        process=Process.sequential,
        memory=True,  # Enable crew memory
        user_id=USER_ID,  # Directly pass user_id to the crew
        memory_provider="mem0",  # Specify the memory provider directly
        verbose=True
    )

# Main POC execution function
def run_poc(destination):
    """Run the POC for CrewAI with Mem0 integration"""
    print(f"\n--- Starting CrewAI + Mem0 POC for {destination} ---\n")

    # Step 1: Initialize memory (only needed once per user)
    initialize_user_memory()

    # Step 2: Create agent
    agent = create_recommendation_agent()

    # Step 3: Create task
    task = create_recommendation_task(agent, destination)

    # Step 4: Setup crew with memory
    crew = setup_memory_crew(agent, task)

    # Step 5: Execute and get results
    print(f"\nGenerating personalized recommendations for {destination}...\n")
    try:
        result = crew.kickoff()
        print("\n--- Results ---\n")
        print(result)
        return result
    except Exception as e:
        print(f"\n--- Error encountered: {str(e)} ---\n")
        print("Debug info:")
        print(f"- Mem0 API key set: {'Yes' if os.environ.get('MEM0_API_KEY') else 'No'}")
        print(f"- OpenAI API key set: {'Yes' if os.environ.get('OPENAI_API_KEY') else 'No'}")
        print(f"- User ID being used: {USER_ID}")
        return None

# Example usage
if __name__ == "__main__":
    # Choose a destination for the POC
    destination = "Kyoto, Japan"

    # Run the POC
    run_poc(destination)