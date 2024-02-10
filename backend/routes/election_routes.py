from models import Election
from services.election_service import ElectionService
from fastapi import APIRouter, Depends, HTTPException
from auth import get_current_user
from typing import List

election_routes = APIRouter()

election_service = ElectionService()

@election_routes.get('/elections', response_model=List[Election])
async def get_all_elections(current_user: dict = Depends(get_current_user)):
    return election_service.get_all_elections()

@election_routes.post('/elections', response_model=Election)
async def create_election(election: Election, current_user: dict = Depends(get_current_user)):
    election_service.create_election(election)
    return election

@election_routes.get('/elections/{election_id}', response_model=Election)
async def get_election(election_id: str, current_user: dict = Depends(get_current_user)):
    election = election_service.get_election(election_id)
    if election:
        return election
    else:
        raise HTTPException(status_code=404, detail="Election not found")
    
    