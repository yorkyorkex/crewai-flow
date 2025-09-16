# Travel Planner Usage Examples

This document shows various ways to use the Travel Planner Agentic System.

## 🎯 Interactive Mode (Recommended)

The most user-friendly way to use the system:

```bash
python main.py
```

### Example Interactive Session:

```
🌍 Welcome to Travel Planner Agentic System!
==================================================
Please provide your travel requirements:

🗺️  Destination (e.g., 'Tokyo, Japan'): Paris, France
📅 Start date (YYYY-MM-DD, e.g., '2024-03-15'): 2024-05-10
📅 End date (YYYY-MM-DD, e.g., '2024-03-22'): 2024-05-15
💰 Total budget in USD (e.g., '2000'): 2500
👥 Number of travelers (e.g., '2'): 2
❤️  Travel preferences: Romantic atmosphere, fine dining, art museums, scenic walks
🎨 Travel styles:
   1. cultural - Focus on culture, history, and traditions
   2. adventurous - Outdoor activities and adventure sports
   3. luxury - High-end experiences and comfort
   4. relaxed - Leisurely pace with rest and relaxation
   5. balanced - Mix of all styles
Choose travel style (1-5 or type style name): luxury

✅ Travel style: luxury

📋 Travel Request Summary:
   🗺️  Destination: Paris, France
   📅 Dates: 2024-05-10 to 2024-05-15
   💰 Budget: $2500.0
   👥 Travelers: 2
   🎨 Style: luxury
   ❤️  Preferences: Romantic atmosphere, fine dining, art museums, scenic walks

Continue with this travel request? (y/n): y

🚀 Starting Travel Planner Agentic System
==================================================
🔍 Researching destination: Paris, France
✅ Destination research completed for Paris, France
📅 Planning itinerary for Paris, France
✅ Itinerary planning completed with 6 days planned
📋 Finalizing travel plan
✅ Travel plan finalized
💾 Saving travel plan
✅ Travel plan saved as ./travel_plan_Paris_France_2024-05-10.json
✅ Readable summary saved as ./travel_plan_Paris_France_2024-05-10.md
```

## 🚀 Quick Demo Mode

For testing or demonstration purposes:

```bash
python main.py --default
```

This uses pre-configured values:

- Destination: Tokyo, Japan
- Dates: 2024-03-15 to 2024-03-22
- Budget: $2000
- Travelers: 2
- Style: Cultural
- Preferences: Cultural experiences, local food, historical sites

## 📊 Workflow Visualization

View the system's workflow:

```bash
python main.py --plot
```

This generates a visual diagram showing:

1. Destination Research → Itinerary Planning → Plan Finalization → Save Results

## 🧪 Testing Input Functionality

Test just the input collection without running the full system:

```bash
python test_input.py
```

This is useful for:

- Testing user input validation
- Debugging input collection
- Understanding the data structure

## 📁 Output Files

The system generates two files for each travel plan:

### JSON File (Machine Readable)

`travel_plan_[destination]_[date].json`

Contains complete structured data:

```json
{
  "request": {
    "destination": "Paris, France",
    "start_date": "2024-05-10",
    "end_date": "2024-05-15",
    "budget": 2500.0,
    "travelers_count": 2,
    "preferences": "Romantic atmosphere, fine dining...",
    "travel_style": "luxury"
  },
  "destination_info": {
    "name": "Paris, France",
    "description": "...",
    "attractions": ["Eiffel Tower", "Louvre Museum", ...]
  },
  "itinerary": {
    "daily_plans": [...]
  }
}
```

### Markdown File (Human Readable)

`travel_plan_[destination]_[date].md`

Formatted for easy reading:

```markdown
# Travel Plan: Paris, France

## Trip Overview

- **Destination**: Paris, France
- **Dates**: 2024-05-10 to 2024-05-15
- **Duration**: 6 days
- **Travelers**: 2
- **Budget**: $2500.0
- **Travel Style**: luxury

## Daily Itinerary

### Day 1 - 2024-05-10

_Day 1 activities focused on logistics experiences_

- **Arrival and Check-in**

  - Arrive at destination and check into accommodation
  - Duration: 2 hours
  - Location: Airport/Hotel

- **Welcome dinner** ($40)
  - Enjoy local cuisine at nearby restaurant
  - Duration: 2 hours
  - Location: Near hotel
```

## 🎨 Customization Examples

### Beach Vacation Example

```
Destination: Maldives
Dates: 2024-06-01 to 2024-06-07
Budget: $5000
Travelers: 2
Style: relaxed
Preferences: Beach activities, water sports, spa treatments, sunset dining
```

### Adventure Trip Example

```
Destination: Nepal, Kathmandu
Dates: 2024-09-15 to 2024-09-25
Budget: $1200
Travelers: 1
Style: adventurous
Preferences: Hiking, mountain views, local culture, budget accommodation
```

### Family Cultural Tour

```
Destination: Rome, Italy
Dates: 2024-07-10 to 2024-07-17
Budget: $3000
Travelers: 4
Style: cultural
Preferences: Historical sites, museums, family-friendly activities, authentic food
```

### Business Trip with Leisure

```
Destination: Singapore
Dates: 2024-04-20 to 2024-04-25
Budget: $2800
Travelers: 1
Style: balanced
Preferences: Business facilities, networking events, local cuisine, shopping
```

## 🔧 Tips for Best Results

1. **Be Specific with Preferences**: Instead of "good food," say "street food markets, local specialties, vegetarian options"

2. **Realistic Budget**: Consider accommodation, meals, activities, and transportation

3. **Travel Style Matching**:

   - Cultural: Museums, historical sites, local traditions
   - Adventurous: Outdoor activities, sports, exploration
   - Luxury: High-end hotels, fine dining, premium experiences
   - Relaxed: Leisurely pace, spa treatments, comfortable accommodations
   - Balanced: Mix of activities and relaxation

4. **Date Formatting**: Always use YYYY-MM-DD format for dates

5. **Group Size Considerations**: Larger groups may need different activity types and logistics

## ❗ Troubleshooting

### Common Issues:

1. **Invalid Date Format**: Use YYYY-MM-DD (e.g., 2024-03-15)
2. **Budget Too Low**: System will suggest realistic minimum budgets
3. **Unrealistic Trip Duration**: Very short (1 day) or very long (>30 days) trips may need adjustment
4. **Vague Preferences**: More specific preferences lead to better recommendations

### Getting Help:

- Check the README.md for installation and setup
- Run `python test_input.py` to verify input functionality
- Use `python main.py --default` for quick testing

---

**Happy travels! 🧳✈️**
