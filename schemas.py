from pydantic import BaseModel
from datetime import date


class StudentSchema(BaseModel):
    id: int = None
    name: str
    birth_date: date = None
    
    
class UserSchema(BaseModel):
    id: int = None
    first_name: str
    last_name: str
    email: str
    username: str
    