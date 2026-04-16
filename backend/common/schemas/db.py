from pydantic import Field

from backend.common.schemas import MongoBaseModel


class User(MongoBaseModel):  # TODO: Update schema as in UserRegister
    username: str = Field(alias="uid")
    hashed_pwd: str
    name: str
    designation: str
    salt: str
