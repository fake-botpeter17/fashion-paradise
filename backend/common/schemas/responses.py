from typing import Optional
from enum import StrEnum

from backend.common.schemas import MongoBaseModel


class ServerResponseStatus(StrEnum):
    Success = "success"
    Error = "error"


class ServerResponse(MongoBaseModel):
    status: ServerResponseStatus
    message: Optional[str] = ""
    data: Optional[dict | list] | None = None
    error: Optional[dict] | None = None
