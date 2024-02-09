from pydantic import BaseModel
from typing import List

class User(BaseModel):
    user_id: str
    username: str
    first_name: str
    last_name: str
    email: str
    address: str
    nationalID: str

class Voter(User):
    pass

class Candidate(User):
    party_name: str
    manifesto: str

class Election(BaseModel):
    election_id: str
    election_name: str
    election_start: str
    election_end: str

class Vote(BaseModel):
    vote_id: str
    voter_id: str 
    candidate_id: str  
    vote_time: str
    vote_location: str


