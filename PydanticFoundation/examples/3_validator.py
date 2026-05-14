from pydantic import BaseModel, field_validator, model_validator, computed_field
#help(field_validator)

class User(BaseModel):
    username: str

    # By default runs with after mode
    # so the workflow is gets in data --> does the conversion(int to str) if 
    # necessary --> runs the field validator method 
    # everything can be considered as part of a constructor
    @field_validator('username')
    def username_length(cls, v):
        if len(v) < 4:
            raise ValueError("Username length should be atleast 4")
        print(v)
        return v

input = {'username':"Soham"}
user1 = User(**input)

class SignUpData(BaseModel):
    password: str
    confirm_password: str

    # depricated 
    # @model_validator(mode='after')
    # def password_match(cls, values):
    #     if values.password != values.confirm_password:
    #         raise ValueError("Passwords do not match")
    #     return values

    @model_validator(mode='after')
    def password_match(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        print("Validated")
        return self
    
input_data = {'password' : "1234", 'confirm_password': "1234"}
user2 = SignUpData(**input_data)

class Product(BaseModel):
    price: float
    quantity: int

    # make property on the go 
    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity
    
input = {'price':100,'quantity':3}
Prod1 = Product(**input)
print(Prod1)


