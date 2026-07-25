from pydantic import BaseModel

class UserV1(BaseModel):
    name: str
    age: int

from pydantic import BaseModel

class UserV2(BaseModel):
    first_name: str
    last_name: str
    email: str
    age: int