#!/usr/bin/env python
"""
Simple interactive launcher for the Travel Planner Agentic System
"""

import sys
import os

# Add the src directory to Python path so we can import our modules
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from travel_planner_agentic_system.main import kickoff, kickoff_with_defaults, plot


def main():
    """Main launcher with options"""
    print("🌍 Travel Planner Agentic System")
    print("=" * 40)
    print("Choose an option:")
    print("1. 🎯 Interactive Planning (Enter your travel details)")
    print("2. 🚀 Quick Demo (Use default Tokyo trip)")
    print("3. 📊 Show Flow Diagram")
    print("4. ❓ Help")
    print()
    
    choice = input("Enter your choice (1-4) or press Enter for interactive: ").strip()
    
    if choice == "" or choice == "1":
        print("\n🎯 Starting Interactive Planning...")
        kickoff()
    elif choice == "2":
        print("\n🚀 Starting Quick Demo...")
        kickoff_with_defaults()
    elif choice == "3":
        print("\n📊 Generating Flow Diagram...")
        plot()
    elif choice == "4":
        show_help()
    else:
        print("Invalid choice. Starting interactive planning...")
        kickoff()


def show_help():
    """Show help information"""
    print("\n❓ Travel Planner Agentic System Help")
    print("=" * 40)
    print("This system helps you plan detailed travel itineraries using AI agents.")
    print()
    print("🎯 Interactive Planning:")
    print("  - Enter your destination, dates, budget, and preferences")
    print("  - AI agents will research the destination and create a detailed itinerary")
    print("  - Get both JSON data and readable Markdown summary")
    print()
    print("🚀 Quick Demo:")
    print("  - Uses pre-configured Tokyo trip for demonstration")
    print("  - Shows the full system workflow without user input")
    print()
    print("📊 Flow Diagram:")
    print("  - Visualizes the workflow steps and agent interactions")
    print()
    print("📁 Output Files:")
    print("  - travel_plan_[destination]_[date].json - Complete data")
    print("  - travel_plan_[destination]_[date].md - Readable summary")
    print()
    print("💡 Command Line Options:")
    print("  python run.py          - Show this menu")
    print("  python main.py         - Direct interactive planning")
    print("  python main.py --default - Quick demo with defaults")
    print("  python main.py --plot  - Show flow diagram")
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Thanks for using Travel Planner Agentic System!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Please check that all dependencies are installed and try again.")