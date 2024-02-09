from services.user_service import UserService
from fastapi import APIRouter, Depends, HTTPException
from auth import get_current_user
from models import Voter, Candidate


user_routes = APIRouter()

user_service = UserService()

@user_routes.route('/voters', methods=['GET'])
def get_all_voters(current_user: dict = Depends(get_current_user)):
    return user_service.get_all_voters()

@user_routes.route('/voters', methods=['POST'])
def create_voter(voter: Voter):
    user_service.create_voter(voter)
    return voter

@user_routes.route('/voters/<voter_id>', methods=['GET'])
def get_voter(voter_id: str, current_user: dict = Depends(get_current_user)):
    voter = user_service.get_voter(voter_id)
    if voter:
        return voter
    else:
        raise HTTPException(status_code=404, detail="Voter not found")
    
@user_routes.route('/candidates', methods=['GET'])
def get_all_candidates():
    return user_service.get_all_candidates()

@user_routes.route('/candidates', methods=['POST'])
def create_candidate(candidate: Candidate):
    user_service.create_candidate(candidate)
    return candidate

@user_routes.route('/candidates/<candidate_id>', methods=['GET'])
def get_candidate(candidate_id: str):
    candidate = user_service.get_candidate(candidate_id)
    if candidate:
        return candidate
    else:
        raise HTTPException(status_code=404, detail="Candidate not found")
    
    

