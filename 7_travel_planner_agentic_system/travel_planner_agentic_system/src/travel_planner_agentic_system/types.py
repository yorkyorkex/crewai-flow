from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel


class TravelRequest(BaseModel):
    """用戶的旅行請求"""
    destination: str
    start_date: str
    end_date: str
    budget: Optional[float] = None
    travelers_count: int = 1
    preferences: Optional[str] = None
    travel_style: Optional[str] = "balanced"  # adventurous, relaxed, cultural, luxury


class DestinationInfo(BaseModel):
    """目的地資訊"""
    name: str
    description: str
    best_time_to_visit: str
    climate: str
    currency: str
    language: str
    attractions: List[str]
    estimated_daily_budget: Optional[float] = None


class Activity(BaseModel):
    """活動項目"""
    name: str
    description: str
    duration: str
    cost: Optional[float] = None
    location: str
    category: str  # sightseeing, dining, entertainment, adventure, cultural


class DayPlan(BaseModel):
    """單日行程計劃"""
    day: int
    date: str
    activities: List[Activity]
    total_estimated_cost: Optional[float] = None
    notes: Optional[str] = None


class TravelItinerary(BaseModel):
    """完整的旅行行程"""
    destination: str
    start_date: str
    end_date: str
    total_days: int
    daily_plans: List[DayPlan]
    total_estimated_budget: Optional[float] = None
    travel_tips: List[str] = []
    emergency_contacts: List[str] = []


class TravelPlan(BaseModel):
    """最終的旅行計劃"""
    request: TravelRequest
    destination_info: DestinationInfo
    itinerary: TravelItinerary
    summary: str