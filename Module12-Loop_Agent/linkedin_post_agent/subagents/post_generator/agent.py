"""
LinkedIn Post Generator Agent

This agent generates the initial LinkedIn post before refinement.
"""

from google.adk.agents.llm_agent import LlmAgent

# Constants
GEMINI_MODEL = "gemini-2.0-flash"

# Define the Initial Post Generator Agent
initial_post_generator = LlmAgent(
    name="InitialPostGenerator",
    model=GEMINI_MODEL,
    instruction="""You are a LinkedIn Post Generator.

    Your task is to create a LinkedIn post about an Agent Development Kit (ADK) bootcamp.
    
    ## CONTENT REQUIREMENTS
    Ensure the post includes:
    1. Excitement about learning into Google's Agent Development Kit
    2. Showcase my github repo https://github.com/Mathews-Tom/Google-ADK-Bootcamp
    2. Specific aspects of ADK learned and demonstrated in the bootcamp:
        - Basic agent implementation (basic-agent)
        - Tool integration (tool-agent)
        - Using LiteLLM (litellm-agent)
        - Managing sessions and memory
        - Persistent storage capabilities
        - Multi-agent orchestration
        - Stateful multi-agent systems
        - Callback systems
        - Sequential agents for pipeline workflows
        - Parallel agents for concurrent operations
        - Loop agents for iterative refinement
    3. Brief statement about improving AI applications
    4. Learn and apply ADK best practices
    5. Understand the simplicity in complexity to build robust AI applications
    6. Clear call-to-action for connections
    
    ## STYLE REQUIREMENTS
    - Professional and conversational tone
    - Between 2000-3000 characters
    - Include emojis
    - Include hashtags
    - Show genuine enthusiasm
    - Highlight practical applications
    
    ## OUTPUT INSTRUCTIONS
    - Return ONLY the post content
    - Do not add formatting markers or explanations
    """,
    description="Generates the initial LinkedIn post to start the refinement process",
    output_key="current_post",
)
