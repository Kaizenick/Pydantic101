#TODO: Create Product model with id, name, price, in_stock

from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool

input = {'id':1,'name':"Mouse",'price':89,'in_stock':True}

p1 = Product(**input)
print(p1)