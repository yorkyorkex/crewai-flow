#!/usr/bin/env python
"""
Simple test of the interactive input functionality
"""

from datetime import datetime
from typing import Optional

# Simple version of TravelRequest for testing
class SimpleTravelRequest:
    def __init__(self, destination, start_date, end_date, budget, travelers_count, preferences, travel_style):
        self.destination = destination
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget
        self.travelers_count = travelers_count
        self.preferences = preferences
        self.travel_style = travel_style


def get_user_input() -> SimpleTravelRequest:
    """獲取用戶輸入的旅行需求"""
    print("🌍 Welcome to Travel Planner Agentic System!")
    print("=" * 50)
    print("Please provide your travel requirements:")
    print()
    
    # Get destination
    destination = input("🗺️  Destination (e.g., 'Tokyo, Japan'): ").strip()
    if not destination:
        destination = "Tokyo, Japan"
        print(f"   Using default: {destination}")
    
    # Get travel dates
    start_date = input("📅 Start date (YYYY-MM-DD, e.g., '2024-03-15'): ").strip()
    if not start_date:
        start_date = "2024-03-15"
        print(f"   Using default: {start_date}")
    
    end_date = input("📅 End date (YYYY-MM-DD, e.g., '2024-03-22'): ").strip()
    if not end_date:
        end_date = "2024-03-22"
        print(f"   Using default: {end_date}")
    
    # Get budget
    budget_input = input("💰 Total budget in USD (e.g., '2000'): ").strip()
    try:
        budget = float(budget_input) if budget_input else 2000.0
    except ValueError:
        budget = 2000.0
        print(f"   Invalid input, using default: ${budget}")
    
    # Get number of travelers
    travelers_input = input("👥 Number of travelers (e.g., '2'): ").strip()
    try:
        travelers_count = int(travelers_input) if travelers_input else 2
    except ValueError:
        travelers_count = 2
        print(f"   Invalid input, using default: {travelers_count}")
    
    # Get preferences
    preferences = input("❤️  Travel preferences (describe what you love): ").strip()
    if not preferences:
        preferences = "We love cultural experiences, local food, and historical sites"
        print(f"   Using default: {preferences}")
    
    # Get travel style
    print("\n🎨 Travel styles:")
    print("   1. cultural - Focus on culture, history, and traditions")
    print("   2. adventurous - Outdoor activities and adventure sports")
    print("   3. luxury - High-end experiences and comfort")
    print("   4. relaxed - Leisurely pace with rest and relaxation")
    print("   5. balanced - Mix of all styles")
    
    style_input = input("Choose travel style (1-5 or type style name): ").strip().lower()
    
    style_mapping = {
        "1": "cultural",
        "2": "adventurous", 
        "3": "luxury",
        "4": "relaxed",
        "5": "balanced",
        "cultural": "cultural",
        "adventurous": "adventurous",
        "luxury": "luxury",
        "relaxed": "relaxed",
        "balanced": "balanced"
    }
    
    travel_style = style_mapping.get(style_input, "cultural")
    if style_input and style_input not in style_mapping:
        print(f"   Unknown style, using default: {travel_style}")
    
    print(f"\n✅ Travel style: {travel_style}")
    print()
    
    # Create and return TravelRequest
    travel_request = SimpleTravelRequest(
        destination=destination,
        start_date=start_date,
        end_date=end_date,
        budget=budget,
        travelers_count=travelers_count,
        preferences=preferences,
        travel_style=travel_style
    )
    
    # Show summary
    print("📋 Travel Request Summary:")
    print(f"   🗺️  Destination: {travel_request.destination}")
    print(f"   📅 Dates: {travel_request.start_date} to {travel_request.end_date}")
    print(f"   💰 Budget: ${travel_request.budget}")
    print(f"   👥 Travelers: {travel_request.travelers_count}")
    print(f"   🎨 Style: {travel_request.travel_style}")
    print(f"   ❤️  Preferences: {travel_request.preferences}")
    print()
    
    confirm = input("Continue with this travel request? (y/n): ").strip().lower()
    if confirm not in ['y', 'yes', '']:
        print("❌ Travel planning cancelled.")
        return None
    
    return travel_request


def main():
    """Test the interactive input"""
    travel_request = get_user_input()
    
    if travel_request:
        print("🎉 Success! Here's what we captured:")
        print(f"Destination: {travel_request.destination}")
        print(f"Dates: {travel_request.start_date} to {travel_request.end_date}")
        print(f"Budget: ${travel_request.budget}")
        print(f"Travelers: {travel_request.travelers_count}")
        print(f"Style: {travel_request.travel_style}")
        print(f"Preferences: {travel_request.preferences}")
        print()
        print("✅ User input functionality is working correctly!")
        print("💡 This input can now be used to configure the TravelPlannerFlow")


if __name__ == "__main__":
    main()