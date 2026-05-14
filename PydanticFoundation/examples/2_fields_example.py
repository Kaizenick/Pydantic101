from pydantic import BaseModel, Field
from typing import Optional

# TODO: Create Employee model
# Fields:
# - id: int
# - name: str (min 3 chars)
# - department: optional str (default 'General')
# - salary: float (must be >= 10000)


# Field(...) --> Required field 
class Employee(BaseModel):
    id: int
    name: str = Field(..., min_length=3, max_length=10, description="Employee Name",examples="Soham Deshpande")
    department: Optional[str] = "General"
    salary: float = Field(ge=10000)

