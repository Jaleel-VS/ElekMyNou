from models import Vote
from db.main import Database

class VoteService:
    def __init__(self):
        self.db = Database()

    def create_vote(self, vote: Vote):
        self.db.collection('votes').add(vote.to_dict())

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
    
    