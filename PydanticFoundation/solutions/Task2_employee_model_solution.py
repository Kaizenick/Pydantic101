from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List, Literal

# 🔥 Practice Problem: E-commerce Order Schema
# You are building a backend system for an order service.
# Requirements:
# Create a Pydantic model called Order with the following:
    # 1. Basic Fields
    # order_id: integer → must be greater than 0
    # user_id: integer → must be greater than 0
    # items: list of item names (strings) → at least 1 item required
    # total_price: float → must be greater than 0
    # 2. Optional Field
    # discount_code: optional string
    # 3. Advanced Field Constraints (IMPORTANT)
    # email: string → must be a valid email format
    # status: string → must be one of: "pending", "shipped", "delivered", "cancelled"

class Order(BaseModel):
    order_id: int = Field(gt=0)
    user_id: int = Field(gt=0)
    items: List[str] = Field(min_length=1)
    total_price: float = Field(gt=0)
    dicount_code: Optional[str] = None
    email:str = Field(pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    built_in_email: EmailStr
    status: Literal["pending", "shipped", "delivered", "cancelled"]


