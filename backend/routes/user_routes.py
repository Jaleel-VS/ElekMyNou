from services.user_service import UserService
from fastapi import APIRouter, Request, Response, HTTPException
from auth import get_current_user


user_routes = APIRouter()

user_service = UserService()

@user_routes.route('/voters', methods=['GET'])
def get_all_voters():
    voters = user_service.get_all_voters()
    return voters

@user_routes.route('/voters', methods=['POST'])
def create_voter(request: Request, response: Response):
    voter = request.json()
    user_service.create_voter(voter)
    response.status_code = 201
    return voter