from models import Vote
from db.main import Database
from fastapi import HTTPException

class VoteService:
    def __init__(self):
        self.db = Database()

    def create_vote(self, vote: Vote):
        # Check if the voter has already voted in the election
        votes = self.get_votes_by_elecion(vote.election_id)

        for v in votes:
            if v.get('voter_id') == vote.voter_id:
                raise HTTPException(status_code=400, detail="Voter has already voted in this election")
            
        self.db.collection('votes').document(vote.vote_id).set(vote.to_dict())
        

    def get_all_votes(self):
        return self.db.collection('votes').get()
    
    def get_vote(self, vote_id: str):
        return self.db.collection('votes').document(vote_id).get()
    
    def get_votes_by_voter(self, voter_id: str):
        return self.db.collection('votes').where('voter_id', '==', voter_id).get()
    
    def get_votes_by_candidate(self, candidate_id: str):
        return self.db.collection('votes').where('candidate_id', '==', candidate_id).get()
    
    def get_votes_by_elecion(self, election_id: str):
        return self.db.collection('votes').where('election_id', '==', election_id).get()
    
