from pydantic import EmailStr
from typing import Optional

from backend.common.schemas.responses import MongoBaseModel


class UserLoginRequest(MongoBaseModel):
    username: str
    password: str


class UserRegisterRequest(MongoBaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    mobile: str
    email: Optional[EmailStr] = ""
