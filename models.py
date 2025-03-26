import strawberry
from enum import Enum

@strawberry.type
class User:
    id: int
    name: str
    age: int
    message: str

@strawberry.type
class ErrorMessageUser:
    id: int
    name: str
    age: int
    message: str

class Messages(Enum):
    SUCCESS="success",
    ERROR_OUT_OF_RANGE="This id is out of range",
    ERROR_AGE_HIGH="This age is very high, we can't handle with it."