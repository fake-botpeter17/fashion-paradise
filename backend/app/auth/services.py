from bcrypt import checkpw

from backend.common.schemas.db import User
from backend.app.auth.schemas.requests import UserLoginRequest
from backend.core.database import users_collection
from backend.common.schemas.responses import ServerResponse, ServerResponseStatus


def login_service(user: UserLoginRequest) -> ServerResponse:
    user_in_db = users_collection.find_one({"uid": user.username})

    if not user_in_db:
        return ServerResponse(
            status=ServerResponseStatus.Error,
            message="User not found!",
            error={"code": "USER_NOT_FOUND"},
        )

    user_in_db = User(**user_in_db)

    print((user_in_db.hashed_pwd[2:-2]), end="\n\n\n")
    if checkpw(
        user.password.encode(), (user_in_db.hashed_pwd[2:-1]).encode()
    ):  # TODO: Fix storage of bytes in db
        return ServerResponse(
            status=ServerResponseStatus.Success,
            message="Login Successful!",
            data={
                "access_token": "should_implement",  # generate_token(user),TODO
                "user": user_in_db.name,
            },
        )

    return ServerResponse(
        status=ServerResponseStatus.Error,
        message="Login Error! Invalid Credentials!",
        error={"code": "INVALID_CREDENTIALS"},
    )
