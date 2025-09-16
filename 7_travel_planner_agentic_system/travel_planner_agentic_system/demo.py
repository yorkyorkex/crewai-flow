#!/usr/bin/env python
"""
Travel Planner Agentic System Demo

This script demonstrates how to use the travel planner with different destinations and preferences.
"""

from travel_planner_agentic_system.main import TravelPlannerFlow
from travel_planner_agentic_system.types import TravelRequest


def demo_tokyo_trip():
    """Demo: Cultural trip to Tokyo"""
    print("🎌 Demo: 7-day Cultural Trip to Tokyo")
    print("=" * 50)
    
    # Create a flow instance
    flow = TravelPlannerFlow()
    
    # Customize the travel request
    flow.state.travel_request = TravelRequest(
        destination="Tokyo, Japan",
        start_date="2024-04-01",
        end_date="2024-04-07",
        budget=1500.0,
        travelers_count=2,
        preferences="We love traditional Japanese culture, temples, gardens, authentic food, and historical sites. Interested in tea ceremonies and local markets.",
        travel_style="cultural"
    )
    
    # Run the planning flow
    flow.kickoff()
    print("✅ Tokyo trip planning completed!")
    print(f"Travel plan saved with {len(flow.state.itinerary.daily_plans)} days of activities")
    print()


def demo_paris_trip():
    """Demo: Romantic trip to Paris"""
    print("🗼 Demo: 5-day Romantic Trip to Paris")
    print("=" * 50)
    
    # Create a flow instance
    flow = TravelPlannerFlow()
    
    # Customize the travel request
    flow.state.travel_request = TravelRequest(
        destination="Paris, France",
        start_date="2024-05-10",
        end_date="2024-05-14",
        budget=2000.0,
        travelers_count=2,
        preferences="Romantic getaway with fine dining, art museums, scenic walks, and cozy cafes. Love photography and wine tasting.",
        travel_style="luxury"
    )
    
    # Run the planning flow
    flow.kickoff()
    print("✅ Paris trip planning completed!")
    print(f"Travel plan saved with {len(flow.state.itinerary.daily_plans)} days of activities")
    print()


def demo_budget_trip():
    """Demo: Budget backpacking trip"""
    print("🎒 Demo: 10-day Budget Trip to Thailand")
    print("=" * 50)
    
    # Create a flow instance
    flow = TravelPlannerFlow()
    
    # Customize the travel request
    flow.state.travel_request = TravelRequest(
        destination="Bangkok, Thailand",
        start_date="2024-06-15",
        end_date="2024-06-24",
        budget=800.0,
        travelers_count=1,
        preferences="Budget backpacking with street food, temples, markets, and meeting locals. Love adventure and authentic experiences.",
        travel_style="adventurous"
    )
    
    # Run the planning flow
    flow.kickoff()
    print("✅ Thailand trip planning completed!")
    print(f"Travel plan saved with {len(flow.state.itinerary.daily_plans)} days of activities")
    print()


def show_flow_diagram():
    """Show the flow process diagram"""
    print("📊 Travel Planner Flow Diagram")
    print("=" * 50)
    
    flow = TravelPlannerFlow()
    flow.plot()


def interactive_demo():
    """Interactive demo that lets user input their own travel requirements"""
    print("🌍 Interactive Travel Planning Demo")
    print("=" * 50)
    print("Create your own custom travel plan!")
    print()
    
    # Import the main kickoff function
    from travel_planner_agentic_system.main import kickoff
    
    # Run interactive planning
    kickoff()


def main():
    """Main demo function"""
    print("🌍 Travel Planner Agentic System Demo")
    print("=" * 60)
    print("Choose how you want to explore the travel planning system:")
    print()
    
    # Show available demos
    demos = {
        "1": ("🎯 Interactive Planning (Custom Input)", interactive_demo),
        "2": ("🎌 Tokyo Cultural Trip (Pre-configured)", demo_tokyo_trip),
        "3": ("🗼 Paris Romantic Trip (Pre-configured)", demo_paris_trip),  
        "4": ("🎒 Thailand Budget Trip (Pre-configured)", demo_budget_trip),
        "5": ("📊 Show Flow Diagram", show_flow_diagram),
        "6": ("🔄 Run All Pre-configured Demos", lambda: [demo() for _, demo in [
            ("Tokyo", demo_tokyo_trip),
            ("Paris", demo_paris_trip), 
            ("Thailand", demo_budget_trip)
        ]])
    }
    
    print("Available options:")
    for key, (description, _) in demos.items():
        print(f"  {key}. {description}")
    print()
    
    # Get user choice
    choice = input("Enter your choice (1-6) or press Enter for interactive planning: ").strip()
    
    if choice == "":
        choice = "1"  # Default to interactive
    
    if choice in demos:
        print()
        demos[choice][1]()  # Execute chosen demo
    else:
        print("Invalid choice, running interactive demo...")
        interactive_demo()
    
    print()
    print("🎉 Demo completed!")
    print()
    print("💡 Tips:")
    print("  - Check generated files: travel_plan_*.json and travel_plan_*.md")
    print("  - Run 'python main.py' for direct interactive planning")
    print("  - Run 'python main.py --default' for quick testing with defaults")
    print("  - Run 'python main.py --plot' to see the flow diagram")


if __name__ == "__main__":
    main()