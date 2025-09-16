# Travel Planner Agentic System

A comprehensive AI-powered travel planning system built with CrewAI Flows. This system uses multiple specialized AI agents to research destinations, plan detailed itineraries, and create personalized travel plans.

## 🌟 Features

- **Destination Research**: AI agents research destinations, costs, culture, and practical information
- **Intelligent Itinerary Planning**: Create day-by-day itineraries with activities, timing, and logistics
- **Budget Management**: Cost estimation and budget-aware planning
- **Cultural Insights**: Local customs, etiquette, and cultural recommendations
- **Personalized Recommendations**: Tailored to travel style and preferences
- **Multiple Output Formats**: JSON data and readable Markdown summaries

## 🏗️ System Architecture

The system follows a Flow-based architecture with specialized crews:

### Flow Structure
1. **Destination Research** → Research destination details, costs, and culture
2. **Itinerary Planning** → Create detailed day-by-day plans
3. **Plan Finalization** → Combine all information into comprehensive plan
4. **Save Results** → Generate JSON and Markdown outputs

### Specialized Crews

#### Destination Research Crew
- **Destination Researcher**: Comprehensive destination information
- **Travel Cost Analyst**: Budget analysis and cost estimation  
- **Cultural Advisor**: Local customs and cultural insights

#### Itinerary Planning Crew
- **Itinerary Planner**: Overall trip structure and daily themes
- **Activity Specialist**: Specific activities and experiences
- **Logistics Coordinator**: Transportation and timing optimization

## 📁 Project Structure

```
travel_planner_agentic_system/
├── src/travel_planner_agentic_system/
│   ├── main.py                 # Main Flow implementation
│   ├── types.py               # Data models (TravelRequest, TravelPlan, etc.)
│   └── crews/
│       ├── destination_research_crew/
│       │   ├── destination_research_crew.py
│       │   └── config/
│       │       ├── agents.yaml
│       │       └── tasks.yaml
│       └── itinerary_planning_crew/
│           ├── itinerary_planning_crew.py
│           └── config/
│               ├── agents.yaml
│               └── tasks.yaml
├── demo.py                    # Demo script with examples
└── README.md                  # This file
```

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```

### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

## 🚀 Quick Start

### Interactive Planning (Recommended)

The easiest way to use the system is through interactive input:

```bash
# Interactive planning with user input
python main.py

# Or test the input functionality
python test_input.py
```

The system will prompt you for:
- 🗺️ Destination (e.g., "Tokyo, Japan")
- 📅 Travel dates (start and end)
- 💰 Budget in USD
- 👥 Number of travelers
- ❤️ Travel preferences
- 🎨 Travel style (cultural, adventurous, luxury, relaxed, balanced)

### Quick Demo with Defaults

```bash
# Use pre-configured Tokyo trip for testing
python main.py --default

# Show the workflow diagram
python main.py --plot
```

### Programmatic Usage

```python
from travel_planner_agentic_system.main import TravelPlannerFlow
from travel_planner_agentic_system.types import TravelRequest

# Create a flow instance
flow = TravelPlannerFlow()

# Set your travel request
flow.state.travel_request = TravelRequest(
    destination="Tokyo, Japan",
    start_date="2024-04-01", 
    end_date="2024-04-07",
    budget=1500.0,
    travelers_count=2,
    preferences="Cultural experiences, temples, local food",
    travel_style="cultural"
)

# Run the planning process
flow.kickoff()
```

### Multiple Demo Options

```python
# Run various pre-configured demos
python demo.py
```

## Running the Project

Multiple ways to run the travel planner:

```bash
# Interactive mode (prompts for user input)
python main.py

# Quick demo with defaults
python main.py --default

# Show workflow diagram
python main.py --plot

# Test input functionality
python test_input.py

# Run demo scenarios
python demo.py

# Using CrewAI CLI
crewai run
```

## 📊 Data Models

### TravelRequest
User's travel requirements and preferences:
- `destination`: Where to travel
- `start_date` / `end_date`: Travel dates
- `budget`: Total budget
- `travelers_count`: Number of travelers
- `preferences`: Travel interests and preferences
- `travel_style`: "cultural", "adventurous", "luxury", "relaxed"

### TravelPlan
Complete travel plan output:
- `request`: Original travel request
- `destination_info`: Researched destination details
- `itinerary`: Day-by-day travel itinerary
- `summary`: Trip overview

## Understanding Your System

The travel_planner_agentic_system is composed of multiple AI agents organized into specialized crews, each with unique roles, goals, and tools. These agents collaborate on a series of tasks to achieve complex travel planning objectives.

## Support

For support, questions, or feedback regarding the {{crew_name}} Crew or crewAI.

- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
