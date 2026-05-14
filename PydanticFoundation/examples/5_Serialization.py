from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags: List[str] = []
    # to change the format on the go!!
    model_config = ConfigDict(json_encoders={datetime: lambda v:v.strftime('%d-%m-%Y %H:%M:%S')})
    model_config = ConfigDict(
    json_encoders={
        bool: lambda v: "positive" if v else "negative"
    }
)

user = User(
    id = 1,
    name="soham",
    email = "soham.deshpande2000@gmail.com",
    is_active=True,
    createdAt=datetime(2026,9,5,8,45),
    address=Address(street="Baner Road", city = "Pune", zip_code="001144"),
    tags=["premium","subscriber"],
)

print(user)

# Using model_dump() -> dict

python_dict = user.model_dump()
print(python_dict)

# Using model_dump_json() -> json

python_json = user.model_dump_json()
print(python_json)