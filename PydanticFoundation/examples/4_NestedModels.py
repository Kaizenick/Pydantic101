from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None

Comment.model_rebuild()

address = Address(street="1613", city="Raleigh", postal_code="27606")
user = User(id=1,name="Soham",address=address)
comment = Comment(id=1,content="Hiii",replies=[Comment(id=2,content="hello",replies=[Comment(id=3,content="Third Comment",replies=None)])])

print(comment)