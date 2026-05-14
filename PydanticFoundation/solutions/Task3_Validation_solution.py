from pydantic import BaseModel, field_validator, Field, computed_field

# TODO: Create Booking model
# Fields:
# - user_id: int
# - room_id: int
# - nights: int (must be >=1)
# - rate_per_night: float
# Also, add computed field: total_amount = nights * rate_per_night

class Booking(BaseModel):
    user_id: int
    room_id: int 
    night: int 
    rate_per_night: float
    
    @field_validator('night')
    def check_nights(cls, night) -> int:
        if(night<1):
            raise ValueError("Value of night should be greater than 1")
        return night
    
    @computed_field
    @property
    def total_amount(self) -> float:
        return self.night * self.rate_per_night


input = {'user_id':1,'room_id':2,'night':2,'rate_per_night':100}
b1 = Booking(**input)

print(b1)