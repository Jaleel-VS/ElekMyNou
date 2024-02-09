from models import Vote
from services.vote_service import VoteService
from fastapi import APIRouter, Depends, HTTPException
from auth import get_current_user
from typing import List

vote_routes = APIRouter()

vote_service = VoteService()

@vote_routes.get('/votes', response_model=List[Vote])
async def get_all_votes(current_user: dict = Depends(get_current_user)):
    return vote_service.get_all_votes()

@vote_routes.post('/votes', response_model=Vote)
async def create_vote(vote: Vote, current_user: dict = Depends(get_current_user)):
    vote_service.create_vote(vote)
    return vote

@vote_routes.get('/votes/{vote_id}', response_model=Vote)
async def get_vote(vote_id: str, current_user: dict = Depends(get_current_user)):
    vote = vote_service.get_vote(vote_id)
    if vote:
        return vote
    else:
        raise HTTPException(status_code=404, detail="Vote not found")
    
