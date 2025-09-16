#!/usr/bin/env python
import asyncio
import json
from datetime import datetime
from typing import Optional

from crewai.flow.flow import Flow, listen, start
from pydantic import BaseModel

from travel_planner_agentic_system.types import (
    TravelRequest, 
    DestinationInfo, 
    TravelItinerary,
    TravelPlan
)

from travel_planner_agentic_system.crews.destination_research_crew.destination_research_crew import DestinationResearchCrew
from travel_planner_agentic_system.crews.itinerary_planning_crew.itinerary_planning_crew import ItineraryPlanningCrew


def get_user_input() -> TravelRequest:
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
    travel_request = TravelRequest(
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
        exit()
    
    return travel_request


class TravelPlannerState(BaseModel):
    # Input from user (will be set dynamically)
    travel_request: Optional[TravelRequest] = None
    
    # Intermediate results
    destination_info: Optional[DestinationInfo] = None
    itinerary: Optional[TravelItinerary] = None
    
    # Final result
    travel_plan: Optional[TravelPlan] = None


class TravelPlannerFlow(Flow[TravelPlannerState]):

    @start()
    def research_destination(self):
        """研究旅行目的地的詳細資訊"""
        print(f"🔍 Researching destination: {self.state.travel_request.destination}")
        
        # Use the actual DestinationResearchCrew
        result = (
            DestinationResearchCrew()
            .crew()
            .kickoff(inputs={
                "destination": self.state.travel_request.destination,
                "travel_dates": f"{self.state.travel_request.start_date} to {self.state.travel_request.end_date}",
                "budget": self.state.travel_request.budget,
                "travelers_count": self.state.travel_request.travelers_count,
                "preferences": self.state.travel_request.preferences
            })
        )
        
        # Extract destination info from the crew result
        # For now, we'll use mock data, but in a full implementation, 
        # you'd parse the result from the crew
        destination_data = result.get("destination_info", {}) if isinstance(result, dict) else {}
        
        # Fallback to mock data if crew doesn't return expected format
        self.state.destination_info = DestinationInfo(
            name=destination_data.get("name", self.state.travel_request.destination),
            description=destination_data.get("description", "A wonderful travel destination with rich culture and attractions"),
            best_time_to_visit=destination_data.get("best_time_to_visit", "Year-round"),
            climate=destination_data.get("climate", "Pleasant climate"),
            currency=destination_data.get("currency", "Local currency"),
            language=destination_data.get("language", "Local language"),
            attractions=destination_data.get("attractions", ["Popular attractions", "Cultural sites", "Local landmarks"]),
            estimated_daily_budget=destination_data.get("estimated_daily_budget", 80.0)
        )
        
        print(f"✅ Destination research completed for {self.state.destination_info.name}")

    @listen(research_destination)
    def plan_itinerary(self):
        """根據目的地資訊規劃詳細行程"""
        print(f"📅 Planning itinerary for {self.state.travel_request.destination}")
        
        # Use the actual ItineraryPlanningCrew
        result = (
            ItineraryPlanningCrew()
            .crew()
            .kickoff(inputs={
                "destination": self.state.travel_request.destination,
                "destination_info": self.state.destination_info.model_dump_json(),
                "start_date": self.state.travel_request.start_date,
                "end_date": self.state.travel_request.end_date,
                "budget": self.state.travel_request.budget,
                "preferences": self.state.travel_request.preferences
            })
        )
        
        # Extract itinerary from the crew result
        # For now, we'll create a comprehensive mock itinerary
        from travel_planner_agentic_system.types import DayPlan, Activity
        from datetime import datetime, timedelta
        
        # Calculate trip duration
        start = datetime.strptime(self.state.travel_request.start_date, "%Y-%m-%d")
        end = datetime.strptime(self.state.travel_request.end_date, "%Y-%m-%d")
        total_days = (end - start).days + 1
        
        # Create sample daily plans
        daily_plans = []
        for day in range(total_days):
            current_date = start + timedelta(days=day)
            
            # Create varied activities based on day
            if day == 0:  # Arrival day
                activities = [
                    Activity(
                        name="Arrival and Check-in",
                        description="Arrive at destination and check into accommodation",
                        duration="2 hours",
                        cost=0.0,
                        location="Airport/Hotel",
                        category="logistics"
                    ),
                    Activity(
                        name="Welcome dinner",
                        description="Enjoy local cuisine at nearby restaurant",
                        duration="2 hours",
                        cost=40.0,
                        location="Near hotel",
                        category="dining"
                    )
                ]
            else:  # Regular days
                activities = [
                    Activity(
                        name=f"Morning activity - Day {day + 1}",
                        description="Explore cultural attractions and landmarks",
                        duration="3 hours",
                        cost=20.0,
                        location="City center",
                        category="cultural"
                    ),
                    Activity(
                        name="Local lunch",
                        description="Try authentic local cuisine",
                        duration="1 hour",
                        cost=15.0,
                        location="Local district",
                        category="dining"
                    ),
                    Activity(
                        name=f"Afternoon exploration - Day {day + 1}",
                        description="Visit markets, parks, or museums",
                        duration="3 hours",
                        cost=25.0,
                        location="Various locations",
                        category="sightseeing"
                    )
                ]
            
            day_plan = DayPlan(
                day=day + 1,
                date=current_date.strftime("%Y-%m-%d"),
                activities=activities,
                total_estimated_cost=sum(activity.cost or 0 for activity in activities),
                notes=f"Day {day + 1} activities focused on {activities[0].category} experiences"
            )
            daily_plans.append(day_plan)
        
        # Calculate total budget
        total_budget = sum(day.total_estimated_cost or 0 for day in daily_plans)
        
        self.state.itinerary = TravelItinerary(
            destination=self.state.travel_request.destination,
            start_date=self.state.travel_request.start_date,
            end_date=self.state.travel_request.end_date,
            total_days=total_days,
            daily_plans=daily_plans,
            total_estimated_budget=total_budget,
            travel_tips=[
                "Research local customs and etiquette before arrival",
                "Keep copies of important documents",
                "Learn basic phrases in the local language",
                "Stay connected with local SIM or international roaming",
                "Respect local dress codes and cultural norms"
            ],
            emergency_contacts=[
                "Local emergency services",
                "Tourist information hotline",
                "Embassy contact information"
            ]
        )
        
        print(f"✅ Itinerary planning completed with {len(self.state.itinerary.daily_plans)} days planned")

    @listen(plan_itinerary)
    def finalize_travel_plan(self):
        """整合所有資訊，生成最終的旅行計劃"""
        print("📋 Finalizing travel plan")
        
        # Create comprehensive travel plan
        self.state.travel_plan = TravelPlan(
            request=self.state.travel_request,
            destination_info=self.state.destination_info,
            itinerary=self.state.itinerary,
            summary=f"Complete {self.state.itinerary.total_days}-day travel plan for {self.state.travel_request.destination} "
                   f"from {self.state.travel_request.start_date} to {self.state.travel_request.end_date}. "
                   f"Estimated budget: ${self.state.itinerary.total_estimated_budget}"
        )
        
        print("✅ Travel plan finalized")

    @listen(finalize_travel_plan)
    def save_travel_plan(self):
        """儲存完整的旅行計劃"""
        print("💾 Saving travel plan")
        
        # Create filename based on destination and dates
        destination_name = self.state.travel_request.destination.replace(", ", "_").replace(" ", "_")
        filename = f"./travel_plan_{destination_name}_{self.state.travel_request.start_date}.json"
        
        # Save as JSON file
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.state.travel_plan.model_dump(), f, indent=2, ensure_ascii=False)
        
        print(f"✅ Travel plan saved as {filename}")
        
        # Also create a readable markdown summary
        md_filename = filename.replace('.json', '.md')
        self._create_markdown_summary(md_filename)
        
        print(f"✅ Readable summary saved as {md_filename}")

    def _create_markdown_summary(self, filename: str):
        """創建旅行計劃的 Markdown 摘要"""
        plan = self.state.travel_plan
        
        markdown_content = f"""# Travel Plan: {plan.destination_info.name}

## Trip Overview
- **Destination**: {plan.destination_info.name}
- **Dates**: {plan.request.start_date} to {plan.request.end_date}
- **Duration**: {plan.itinerary.total_days} days
- **Travelers**: {plan.request.travelers_count}
- **Budget**: ${plan.itinerary.total_estimated_budget}
- **Travel Style**: {plan.request.travel_style}

## Destination Information
{plan.destination_info.description}

- **Best Time to Visit**: {plan.destination_info.best_time_to_visit}
- **Climate**: {plan.destination_info.climate}
- **Currency**: {plan.destination_info.currency}
- **Language**: {plan.destination_info.language}

### Top Attractions
"""
        
        for attraction in plan.destination_info.attractions:
            markdown_content += f"- {attraction}\n"
        
        markdown_content += "\n## Daily Itinerary\n"
        
        for day_plan in plan.itinerary.daily_plans:
            markdown_content += f"\n### Day {day_plan.day} - {day_plan.date}\n"
            if day_plan.notes:
                markdown_content += f"*{day_plan.notes}*\n\n"
            
            for activity in day_plan.activities:
                cost_info = f" (${activity.cost})" if activity.cost else ""
                markdown_content += f"- **{activity.name}**{cost_info}\n"
                markdown_content += f"  - {activity.description}\n"
                markdown_content += f"  - Duration: {activity.duration}\n"
                markdown_content += f"  - Location: {activity.location}\n\n"
        
        markdown_content += "\n## Travel Tips\n"
        for tip in plan.itinerary.travel_tips:
            markdown_content += f"- {tip}\n"
        
        markdown_content += "\n## Emergency Contacts\n"
        for contact in plan.itinerary.emergency_contacts:
            markdown_content += f"- {contact}\n"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(markdown_content)


def kickoff():
    """啟動旅行規劃流程"""
    # Get user input for travel requirements
    travel_request = get_user_input()
    
    print("🚀 Starting Travel Planner Agentic System")
    print("=" * 50)
    
    # Create flow and set user's travel request
    travel_planner_flow = TravelPlannerFlow()
    travel_planner_flow.state.travel_request = travel_request
    
    # Start the planning process
    travel_planner_flow.kickoff()


def kickoff_with_defaults():
    """啟動旅行規劃流程（使用預設值，用於測試）"""
    print("🚀 Starting Travel Planner Agentic System (Default Values)")
    print("=" * 50)
    
    # Create flow with default travel request
    travel_planner_flow = TravelPlannerFlow()
    travel_planner_flow.state.travel_request = TravelRequest(
        destination="Tokyo, Japan",
        start_date="2024-03-15",
        end_date="2024-03-22",
        budget=2000.0,
        travelers_count=2,
        preferences="We love cultural experiences, local food, and historical sites",
        travel_style="cultural"
    )
    
    travel_planner_flow.kickoff()


def plot():
    """顯示流程圖"""
    travel_planner_flow = TravelPlannerFlow()
    travel_planner_flow.plot()


if __name__ == "__main__":
    # Check if user wants to use interactive mode or defaults
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--default":
        kickoff_with_defaults()
    elif len(sys.argv) > 1 and sys.argv[1] == "--plot":
        plot()
    else:
        kickoff()
