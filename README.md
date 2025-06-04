# Google Agent Development Kit (ADK) Bootcamp

**Welcome to the Google Agent Development Kit (ADK) Bootcamps!**

This repository is your comprehensive, hands-on guide to mastering LLM-powered agent development using Google’s Agent Development Kit (ADK). Designed for both beginners and experienced developers, these bootcamps walk you through the nitty-gritty of ADK — from core concepts to advanced patterns — using real-world examples, modular lessons, and best practices to accelerate your learning.

## Project Overview

The ADK Crash Course is designed to help you:

- Understand the fundamentals of LLM-powered agents.
- Explore a variety of agent patterns, from basic to advanced (multi-agent, stateful, callback-driven, and more).
- Learn by example, with each module focusing on a specific concept or capability.
- Use modern Python tooling for efficient development and reproducibility.

## Installation

This project uses [`uv`](https://github.com/astral-sh/uv), a modern, ultra-fast Python package manager and virtual environment tool.  
**If you don't have `uv` installed, follow these steps:**

### 1. Install `uv`

#### macOS / Linux / Windows (with Python ≥3.8)

```bash
# Install via pipx (recommended)
pipx install uv

# Or install via Homebrew (macOS/Linux)
brew install uv

# Or install via pip (if pipx/brew unavailable)
pip install uv
```

> For more installation options, see the [uv documentation](https://github.com/astral-sh/uv).

### 2. Set Up the Project Environment

You only need to create one environment for all modules:

```bash
# Create and activate a virtual environment using uv
uv venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install all dependencies
uv sync
```

### 3. Running Examples

Each module is self-contained. To run an example:

1. Activate your environment (if not already active):

   ```bash
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Navigate to the desired module directory.
3. Follow the module's README for specific run instructions.

## Setting Up API Keys

1. Create a Google Cloud account: <https://cloud.google.com/?hl=en>
2. Create a new project.
3. Go to <https://aistudio.google.com/apikey>
4. Create an API key.
5. Assign the key to your project.
6. Connect to a billing account.

Each example folder contains a `.env.example` file. For each project you want to run:

1. Navigate to the example folder.
2. Rename `.env.example` to `.env`.
3. Open `.env` and replace the placeholder with your API key:

   ```text
   GOOGLE_API_KEY=your_api_key_here
   ```

Repeat this for each example you wish to run.

## Module Overview

Below is a summary of each module in this course:

### Module 1: Basic Agent

**Purpose:** Introduction to the simplest form of ADK agents. Learn how to create a basic agent that can respond to user queries.

### Module 2: Tool Agent

**Purpose:** Enhance agents with tools, enabling them to perform actions beyond text generation (e.g., calling APIs, using utilities).

### Module 3: LiteLLM Agent

**Purpose:** Demonstrates using LiteLLM to abstract LLM provider details, making it easy to switch between different language models.

### Module 4: Structured Outputs

**Purpose:** Shows how to use Pydantic models and output schemas to ensure agents return structured, validated responses.

### Module 5: Sessions and State

**Purpose:** Explores maintaining conversational state and memory across multiple interactions using session management.

### Module 6: Persistent Storage

**Purpose:** Introduces techniques for persisting agent data across sessions and application restarts, enabling long-term memory.

### Module 7: Multi Agent

**Purpose:** Orchestrates multiple specialized agents working together to solve complex, multi-faceted tasks.

### Module 8: Stateful Multi Agent

**Purpose:** Builds on multi-agent systems by maintaining and updating state throughout complex, multi-turn conversations.

### Module 9: Callbacks

**Purpose:** Implements event callbacks to monitor, log, or react to agent behaviors in real-time.

### Module 10: Sequential Agent

**Purpose:** Creates pipeline workflows where agents operate in a defined sequence, passing information step-by-step.

### Module 11: Parallel Agent

**Purpose:** Leverages concurrent operations with parallel agents for improved efficiency and performance.

### Module 12: Loop Agent

**Purpose:** Builds agents that iteratively refine their outputs through feedback loops, enabling self-improvement.

## Official Documentation

For more detailed information, check out the official ADK documentation:  
<https://cloud.google.com/agent-development-kit/docs>

## Contributing

Contributions are welcome! To contribute:

1. Fork this repository.
2. Create a new branch for your feature or fix.
3. Make your changes following best practices and ensure all examples remain functional.
4. Submit a pull request with a clear description of your changes.

Please see the [LICENSE](LICENSE) file for information about usage and distribution.

## License

This project is licensed under the terms of the [MIT License](LICENSE).
