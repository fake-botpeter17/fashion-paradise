from pydantic import BaseModel, Field, field_validator
from bson import ObjectId
from typing import Optional


class MongoBaseModel(BaseModel):
    id: Optional[str] = Field(alias="_id", default=None)

    @field_validator("id", mode="before")
    @classmethod
    def convert_objectid_to_str(cls, value):
        if isinstance(value, ObjectId):
            return str(value)
        return value

    def to_cleaned_dict(self, inc_ob_id: bool = False, include: set | None = None):
        if inc_ob_id:
            return self.model_dump(include=include)
        return self.model_dump(exclude={"id"}, include=include)
