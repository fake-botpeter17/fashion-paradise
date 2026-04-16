from flask import request

from backend.app.auth.services import login_service
from backend.app.auth.schemas.requests import UserLoginRequest
from backend.app.auth import auth_bp


@auth_bp.route("/login", methods=["GET"])
def login():
    data = request.args
    username = data.get("username", "")
    password = data.get("password", "")
    user_credentials = UserLoginRequest(username=username, password=password)
    response = login_service(user_credentials)

    if getattr(response, "error", False):
        return response.to_cleaned_dict(), 401

    return response.to_cleaned_dict(), 200


@auth_bp.route("/refresh", methods=["POST"])
def refresh_token():
    raise NotImplementedError


@auth_bp.route("/logout", methods=["POST"])
def logout():
    raise NotImplementedError


@auth_bp.route("/health")
def health():
    return {"status": True}
